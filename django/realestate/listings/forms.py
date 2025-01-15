from django import forms

class SearchForm(forms.Form):
    cena_min = forms.DecimalField(required=False, label="Cena od", min_value=0)
    cena_max = forms.DecimalField(required=False, label="Cena do", min_value=0)
    powierzchnia_min = forms.DecimalField(required=False, label="Powierzchnia od", min_value=0)
    powierzchnia_max = forms.DecimalField(required=False, label="Powierzchnia do", min_value=0)
    pokoje_min = forms.IntegerField(required=False, label="Liczba pokoi od", min_value=0)
    pokoje_max = forms.IntegerField(required=False, label="Liczba pokoi do", min_value=0)
    
class PredictionForm(forms.Form):
    powierzchnia = forms.FloatField(label="Powierzchnia całkowita (m²)")
    liczba_pokoi = forms.IntegerField(label="Liczba pokoi")
    pietro = forms.IntegerField(label="Piętro")
    liczba_pieter = forms.IntegerField(label="Liczba pięter")
    garaz = forms.IntegerField(label="Garaż (0 - nie, 1 - tak)", min_value=0, max_value=1)
    miejsce_parkingowe = forms.IntegerField(label="Miejsce parkingowe (0 - nie, 1 - tak)", min_value=0, max_value=1)
    dzielnica_num = forms.IntegerField(label="Numer dzielnicy")