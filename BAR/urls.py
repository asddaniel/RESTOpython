from django.urls import path
from .views import StockListCreateAPIView, StockRetrieveUpdateDestroyAPIView, VenteListCreateAPIView, VenteRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('stocks/', StockListCreateAPIView.as_view(), name='stock-list-create'),
    path('stocks/<int:pk>/', StockRetrieveUpdateDestroyAPIView.as_view(), name='stock-retrieve-update-destroy'),
    path('ventes/', VenteListCreateAPIView.as_view(), name='vente-list-create'),
    path('ventes/<int:pk>/', VenteRetrieveUpdateDestroyAPIView.as_view(), name='vente-retrieve-update-destroy'),
]
