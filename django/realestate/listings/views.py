from django import forms
from django.shortcuts import render
import joblib
import pandas as pd
from .forms import PredictionForm
from .forms import SearchForm
from .models import Aktualne
import base64
from io import BytesIO
import matplotlib.pyplot as plt

def home(request):
    return render(request, 'listings/home.html')

pipeline = joblib.load(r'model.pkl')

def plot_dzielnica(request):
    districts_distance_map = {
        1: ['Centrum', 'Śródmieście', 'Koszutka', 'Bogucice'],
        2: ['Os. Paderewskiego', 'Muchowiec', 'Załęże', 'Osiedle Wincentego Witosa', 'Witosa', 'Osiedle Tysiąclecia'],
        3: ['Dąb', 'Wełnowiec-Józefowiec', 'Józefowiec', 'Ligota-Panewniki', 'Ligota', 'Brynów-Osiedle Zgrzebnioka', 'Brynów'],
        4: ['Załęska Hałda', 'Brynów', 'Zawodzie', 'Dąbrówka Mała', 'Szopienice-Burowiec', 'Szopienice'],
        5: ['Janów-Nikiszowiec', 'Nikiszowiec', 'Giszowiec', 'Murcki', 'Piotrowice-Ochojec', 'Piotrowice', 'Ochojec', 'Zarzecze', 'Kostuchna', 'Podlesie']
    }

    grouped_districts = {}
    for group_number, districts in districts_distance_map.items():
        group_label = f"Grupa {group_number}"
        grouped_districts[group_number] = {'label': group_label, 'districts': districts}

    data = fetch_data_from_db()
    dzielnice = data['dzielnica_num'].unique()

    plot_buffer = None
    stats = None

    if request.method == 'GET' and 'dzielnica_num' in request.GET:
            selected_group_number = int(request.GET['dzielnica_num'])  
            selected_group_label = grouped_districts.get(selected_group_number, {}).get('label', 'Nieznana grupa') 
            print('Wybrana grupa: ', selected_group_label)
            
            plot_buffer, stats = plot_for_dzielnica(selected_group_number)

    return render(request, 'listings/plots.html', {'dzielnice': dzielnice, 'plot_buffer': plot_buffer, 'stats': stats, 'grouped_districts': grouped_districts})


def fetch_data_from_db():
    offers = Aktualne.objects.all()
    data = pd.DataFrame(list(offers.values('dzielnica_num', 'cena', 'powierzchnia_calkowita', 'liczba_pokoi')))
    return data

def plot_for_dzielnica(selected_dzielnica):
    print('wlazlem2')
    data = fetch_data_from_db()
    print('data: ', data['dzielnica_num'].value_counts())
    try:
        selected_dzielnica = int(selected_dzielnica)
    except ValueError:
        print(f"Nie udało się skonwertować {selected_dzielnica} na liczbę.")
        return None
    subset = data[data['dzielnica_num'] == selected_dzielnica]

    if subset.empty:
        print(f"Brak danych dla dzielnicy {selected_dzielnica}")
        return None

    average_price = subset['cena'].mean()
    median_price = subset['cena'].median()
    std_price = subset['cena'].std()
    
    average_area = subset['powierzchnia_calkowita'].mean()
    median_area = subset['powierzchnia_calkowita'].median()
    std_area = subset['powierzchnia_calkowita'].std()
    
    average_rooms = subset['liczba_pokoi'].mean()
    median_rooms = subset['liczba_pokoi'].median()

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(subset['powierzchnia_calkowita'], subset['cena'], alpha=0.7)
    ax.set_title(f"Dystrybucja Cena do Powierzchni dla {selected_dzielnica}")
    ax.set_xlabel("Powierzchnia (m²)")
    ax.set_ylabel("Cena")

    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    stats = {
        'average_price': average_price,
        'median_price': median_price,
        'std_price': std_price,
        'average_area': average_area,
        'median_area': median_area,
        'std_area': std_area,
        'average_rooms': average_rooms,
        'median_rooms': median_rooms
    }

    return img_base64, stats

    
def search_offers(request):
    form = SearchForm(request.GET or None)
    results = []

    data = fetch_data_from_db()
    dzielnice = data['dzielnica_num'].unique()

    if form.is_valid():
        filters = {}
        if form.cleaned_data.get('cena_min') is not None:
            filters['cena__gte'] = form.cleaned_data['cena_min']
        if form.cleaned_data.get('cena_max') is not None:
            filters['cena__lte'] = form.cleaned_data['cena_max']
        if form.cleaned_data.get('powierzchnia_min') is not None:
            filters['powierzchnia_calkowita__gte'] = form.cleaned_data['powierzchnia_min']
        if form.cleaned_data.get('powierzchnia_max') is not None:
            filters['powierzchnia_calkowita__lte'] = form.cleaned_data['powierzchnia_max']
        if form.cleaned_data.get('pokoje_min') is not None:
            filters['liczba_pokoi__gte'] = form.cleaned_data['pokoje_min']
        if form.cleaned_data.get('pokoje_max') is not None:
            filters['liczba_pokoi__lte'] = form.cleaned_data['pokoje_max']

        results = Aktualne.objects.filter(**filters).values('lokalizacja', 'cena', 'powierzchnia_calkowita', 'liczba_pokoi', 'url')

    return render(request, 'listings/search.html', {'form': form, 'results': results, 'dzielnice': dzielnice})

def predict_price(request):
    print("wlazlem")
    prediction = None
    if request.method == 'POST':
        print("wlazlem2")
        form = PredictionForm(request.POST)
        try:
            print("wlazlem3")
            powierzchnia = float(request.POST.get('powierzchnia'))
            liczba_pokoi = int(request.POST.get('liczba_pokoi'))
            pietro = int(request.POST.get('pietro', 0))  
            liczba_pieter = int(request.POST.get('liczba_pieter', 0))
            garaz = request.POST.get('garaz') == 'on'  
            miejsce_parkingowe = request.POST.get('miejsce_parkingowe') == 'on' 
            dzielnica_num = int(request.POST.get('dzielnica_num'))
            print(f"Input values: {powierzchnia}, {liczba_pokoi}, {pietro}, {liczba_pieter}, {garaz}, {miejsce_parkingowe}, {dzielnica_num}")
            if any(val <= 0 for val in [powierzchnia, liczba_pokoi, pietro, liczba_pieter, dzielnica_num]):
                raise ValueError("Wartości liczbowe muszą być większe od 0")
            if pietro and liczba_pieter:
                if pietro > liczba_pieter:
                    raise forms.ValidationError("Pietro nie moze byc wieksze od liczby pieter!")
            
            new_data = pd.DataFrame({
                'Powierzchnia całkowita': [powierzchnia],
                'Liczba pokoi': [liczba_pokoi],
                'Piętro': [pietro],
                'Liczba pięter': [liczba_pieter],
                'garaż': [garaz],
                'miejsce parkingowe': [miejsce_parkingowe],
                'dzielnica_num': [dzielnica_num]
            })
            try:
                prediction = pipeline.predict(new_data)[0]
            except Exception as e:
                print(f"Prediction error: {e}")
                prediction = None
        except (ValueError, TypeError) as e:
            print(f"Error processing form data: {e}")
            prediction = None

    else:
        form = PredictionForm()

    return render(request, 'listings/prediction.html', {
        'form': form,
        'prediction': prediction
    })