from rest_framework import generics
from .models import StockModel, VenteModel
from .serializers import StockSerializer, VenteSerializer

class StockListCreateAPIView(generics.ListCreateAPIView):
    queryset = StockModel.objects.all()
    serializer_class = StockSerializer

class StockRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockModel.objects.all()
    serializer_class = StockSerializer

class VenteListCreateAPIView(generics.ListCreateAPIView):
    queryset = VenteModel.objects.all()
    serializer_class = VenteSerializer

class VenteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VenteModel.objects.all()
    serializer_class = VenteSerializer
