from rest_framework import generics
from .models import Plat, Commandes, CommandItems, PlatCategorie, Boisson, BoissonCategorie
from .serializers import PlatSerializer, PlatCategorieSerializer, CommandeSerializer, CommandItemSerializer, BoissonCategorieSerializer, BoissonSerializer

class PlatListCreateAPIView(generics.ListCreateAPIView):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer

class PlatRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer

class PlatCategorieListCreateAPIView(generics.ListCreateAPIView):
    queryset = PlatCategorie.objects.all()
    serializer_class = PlatCategorieSerializer

class PlatCategorieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlatCategorie.objects.all()
    serializer_class = PlatCategorieSerializer

class BoissonCategorieListCreateAPIView(generics.ListCreateAPIView):
    queryset = BoissonCategorie.objects.all()
    serializer_class = BoissonCategorieSerializer

class BoissonCategorieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlatCategorie.objects.all()
    serializer_class = BoissonCategorieSerializer

class CommandeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Commandes.objects.all()
    serializer_class = CommandeSerializer

class CommandeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commandes.objects.all()
    serializer_class = CommandeSerializer

class BoissonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Boisson.objects.all()
    serializer_class = BoissonSerializer

class BoissonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boisson.objects.all()
    serializer_class = BoissonSerializer


class CommandeItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = CommandItems.objects.all()
    serializer_class = CommandItemSerializer

class CommandeItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommandItems.objects.all()
    serializer_class = CommandItemSerializer

