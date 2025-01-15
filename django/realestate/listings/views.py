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

pipeline = joblib.load(r'C:\Users\PC\Desktop\scrapping_danych\model.pkl')

def plot_dzielnica(request):
    data = fetch_data_from_db()
    dzielnice = data['dzielnica_num'].unique()

    plot_buffer = None
    stats = None

    if request.method == 'GET' and 'dzielnica' in request.GET:
        selected_dzielnica = request.GET['dzielnica']
        print('Wybrana dzielnica: ', selected_dzielnica)
        plot_buffer, stats = plot_for_dzielnica(selected_dzielnica)

    return render(request, 'listings/plots.html', {'dzielnice': dzielnice, 'plot_buffer': plot_buffer, 'stats': stats})


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
    prediction = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            powierzchnia = form.cleaned_data['powierzchnia']
            liczba_pokoi = form.cleaned_data['liczba_pokoi']
            pietro = form.cleaned_data['pietro']
            liczba_pieter = form.cleaned_data['liczba_pieter']
            garaz = form.cleaned_data['garaz']
            miejsce_parkingowe = form.cleaned_data['miejsce_parkingowe']
            dzielnica_num = form.cleaned_data['dzielnica_num']

            new_data = pd.DataFrame({
                'Powierzchnia całkowita': [powierzchnia],
                'Liczba pokoi': [liczba_pokoi],
                'Piętro': [pietro],
                'Liczba pięter': [liczba_pieter],
                'garaż': [garaz],
                'miejsce parkingowe': [miejsce_parkingowe],
                'dzielnica_num': [dzielnica_num]
            })
            prediction = pipeline.predict(new_data)[0]

    else:
        form = PredictionForm()

    return render(request, 'listings/prediction.html', {
        'form': form,
        'prediction': prediction
    })