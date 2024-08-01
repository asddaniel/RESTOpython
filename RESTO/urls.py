from django.urls import path
from .views import *


urlpatterns = [
    path('plats', PlatListCreateAPIView.as_view(), name='plat-list-create'),
    path('plats/<int:pk>', PlatRetrieveUpdateDestroyAPIView.as_view(), name='plat-retrieve-update-destroy'),
    path('platcategories', PlatCategorieListCreateAPIView.as_view(), name='platcategorie-list-create'),
    path('platcategorie/<int:pk>', PlatCategorieRetrieveUpdateDestroyAPIView.as_view(), name='platcategorie-retrieve-update-destroy'),
    path('boissons', BoissonListCreateAPIView.as_view(), name='boisson-list-create'),
    path('boissons/<int:pk>', BoissonRetrieveUpdateDestroyAPIView.as_view(), name='boisson-retrieve-update-destroy'),
    path('boissonscategories', BoissonCategorieListCreateAPIView.as_view(), name='plat-list-create'),
    path('boissonscategories/<int:pk>', BoissonCategorieRetrieveUpdateDestroyAPIView.as_view(), name='boissonscategorie-retrieve-update-destroy'),
    path('commandes', CommandeListCreateAPIView.as_view(), name='commandes-list-create'),
    path('commandes/<int:pk>', CommandeRetrieveUpdateDestroyAPIView.as_view(), name='commande-retrieve-update-destroy'),
    path('commandItems', CommandeItemListCreateAPIView.as_view(), name='commandeItem-list-create'),
    path('commandItems/<int:pk>', CommandeItemRetrieveUpdateDestroyAPIView.as_view(), name='commandeItem-retrieve-update-destroy'),


]
