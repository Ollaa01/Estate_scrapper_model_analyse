Portal Nieruchomościowy - Django Application
![stronatyt](https://github.com/user-attachments/assets/3e698e75-9f4f-4681-8f4a-0d444b4e0708)

Opis projektu
Portal Nieruchomościowy to aplikacja internetowa stworzona w Django (Python), która umożliwia użytkownikom:
Wyszukiwanie ofert nieruchomości: Użytkownik może przeglądać oferty lokalne, korzystając wyszukiwarki.
Analizę rynku: Aplikacja przedstawia trendy i statystyki dotyczące rynku nieruchomości w Katowicach.
Przewidywanie cen nieruchomości: Dzięki wbudowanemu modelowi uczenia maszynowego aplikacja może przewidzieć cenę nieruchomości na podstawie określonych parametrów.

Funkcjonalności
Scrapowanie danych:
Aplikacja wykorzystuje dwa scrappery, które zbierają dane z serwisów:
Otodom.pl
Domiporta.pl
Pobierane dane dotyczą ofert mieszkań w Katowicach.

Wyszukiwarka ofert:
![wyszukiwarka](https://github.com/user-attachments/assets/5828fc5a-6cea-4caf-9ac9-01fbf1679e48)
Możliwość przeglądania ofert według wybranych kryteriów, takich jak cena, liczba pokoi, powierzchnia.

Analiza rynku:
![analiza](https://github.com/user-attachments/assets/0d79aa3c-2298-43eb-9993-8a47bf581675)
![analiza2](https://github.com/user-attachments/assets/9d5bcff2-5f00-494b-9977-f6d2d1ceff69)
Wykres i statystyki przedstawiające sytuację na rynku nieruchomości w Katowicach w wybranej grupie dzielnic.

Model predykcji cen:
![model](https://github.com/user-attachments/assets/e295adac-59fc-4724-b814-dd165844ba7b)
Model uczenia maszynowego trenuje się na danych zebranych przez scrappery, aby przewidywać cenę nieruchomości w oparciu o wprowadzone dane.

Technologie użyte w projekcie
Backend: Django (Python)
Baza danych: SQLite 
Scrappery: Python + BeautifulSoup/Requests

Plany rozwoju
Dodanie kolejnych miast do scrapowania i analizy.
Rozszerzenie funkcji modelu predykcji.
Ulepszenie interfejsu użytkownika.
