from django.db import models


class Aktualne(models.Model):
    cena = models.FloatField(db_column='Cena', blank=True, null=True)
    cena_za_m2 = models.FloatField(db_column='Cena_za_m2', blank=True, null=True)
    lokalizacja = models.TextField(db_column='Lokalizacja', blank=True, null=True)
    powierzchnia_calkowita = models.FloatField(db_column='Powierzchnia_calkowita', blank=True, null=True)
    liczba_pokoi = models.IntegerField(db_column='Liczba_pokoi', blank=True, null=True)
    piętro = models.TextField(db_column='Piętro', blank=True, null=True)
    typ_budynku = models.TextField(db_column='Typ_budynku', blank=True, null=True)
    rok_budowy = models.TextField(db_column='Rok_budowy', blank=True, null=True)
    typ_ogloszeniodawcy = models.TextField(db_column='Typ_ogloszeniodawcy', blank=True, null=True)
    url = models.TextField(db_column='URL', blank=True, null=True)
    forma_wlasności = models.TextField(db_column='Forma_wlasności', blank=True, null=True)
    dostępne_od = models.TextField(db_column='Dostępne_od', blank=True, null=True)
    stan_wykończenia = models.TextField(db_column='Stan_wykończenia', blank=True, null=True)
    rynek = models.TextField(db_column='Rynek', blank=True, null=True)
    winda = models.IntegerField(db_column='Winda', blank=True, null=True)
    ogrzewanie = models.IntegerField(db_column='Ogrzewanie', blank=True, null=True)
    województwo = models.TextField(db_column='Województwo', blank=True, null=True)
    miasto = models.TextField(db_column='Miasto', blank=True, null=True)
    dzielnica = models.TextField(db_column='Dzielnica', blank=True, null=True)
    ulica = models.TextField(db_column='Ulica', blank=True, null=True)
    liczba_pięter = models.TextField(db_column='Liczba_pięter', blank=True, null=True)
    balkon = models.IntegerField(db_column='Balkon', blank=True, null=True)
    piwnica = models.IntegerField(db_column='Piwnica', blank=True, null=True)
    garaz = models.IntegerField(db_column='Garaz', blank=True, null=True)
    miejsce_parkingowe = models.IntegerField(db_column='Miejsce_parkingowe', blank=True, null=True)
    ogrzewanie_rodzaj = models.TextField(db_column='Ogrzewanie_rodzaj', blank=True, null=True)
    ochrona = models.IntegerField(db_column='Ochrona', blank=True, null=True)
    ogloszeniodawca = models.TextField(db_column='Ogłoszeniodawca', blank=True, null=True)
    dzielnica_num = models.IntegerField(db_column='Dzielnica_num', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aktualne'


class Archiwalne(models.Model):
    cena = models.TextField(db_column='Cena', blank=True, null=True)
    cena_za_m2 = models.TextField(db_column='Cena_za_m2', blank=True, null=True)
    lokalizacja = models.TextField(db_column='Lokalizacja', blank=True, null=True)
    powierzchnia_calkowita = models.TextField(db_column='Powierzchnia_calkowita', blank=True, null=True)
    liczba_pokoi = models.IntegerField(db_column='Liczba_pokoi', blank=True, null=True)
    piętro = models.TextField(db_column='Piętro', blank=True, null=True)
    typ_budynku = models.TextField(db_column='Typ_budynku', blank=True, null=True)
    rok_budowy = models.TextField(db_column='Rok_budowy', blank=True, null=True)
    typ_ogloszeniodawcy = models.TextField(db_column='Typ_ogloszeniodawcy', blank=True, null=True)
    url = models.TextField(db_column='URL', blank=True, null=True)
    forma_wlasnosci = models.TextField(db_column='Forma_wlasnosci', blank=True, null=True)
    dostępne_od = models.TextField(db_column='Dostepne_od', blank=True, null=True)
    stan_wykonczenia = models.TextField(db_column='Stan_wykonczenia', blank=True, null=True)
    rynek = models.TextField(db_column='Rynek', blank=True, null=True)
    winda = models.IntegerField(db_column='Winda', blank=True, null=True)
    ogrzewanie = models.IntegerField(db_column='Ogrzewanie', blank=True, null=True)
    województwo = models.TextField(db_column='Wojewodztwo', blank=True, null=True)
    miasto = models.TextField(db_column='Miasto', blank=True, null=True)
    dzielnica = models.TextField(db_column='Dzielnica', blank=True, null=True)
    ulica = models.TextField(db_column='Ulica', blank=True, null=True)
    liczba_pieter = models.TextField(db_column='Liczba_pieter', blank=True, null=True)
    balkon = models.IntegerField(db_column='Balkon', blank=True, null=True)
    piwnica = models.IntegerField(db_column='Piwnica', blank=True, null=True)
    garaz = models.IntegerField(db_column='Garaz', blank=True, null=True)
    miejsce_parkingowe = models.IntegerField(db_column='Miejsce_parkingowe', blank=True, null=True)
    ogrzewanie_rodzaj = models.TextField(db_column='Ogrzewanie_rodzaj', blank=True, null=True)
    ochrona = models.IntegerField(db_column='Ochrona', blank=True, null=True)
    ogloszeniodawca = models.TextField(db_column='Ogłoszeniodawca', blank=True, null=True)
    dzielnica_num = models.IntegerField(db_column='Dzielnica_num', blank=True, null=True)
    data = models.TextField(db_column='Data', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'archiwalne'
