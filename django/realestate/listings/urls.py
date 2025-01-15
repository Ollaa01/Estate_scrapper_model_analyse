from django.urls import path
from .views import search_offers
from .views import plot_dzielnica
from .views import predict_price
from .views import home

urlpatterns = [
    path('', home, name='home'),  
    path('search/', search_offers, name='search'), 
    path('plots', plot_dzielnica, name='plots'),
    path('predict/', predict_price, name='predict_price'),
]
