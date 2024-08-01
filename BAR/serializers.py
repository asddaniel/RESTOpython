from rest_framework import serializers
from .models import StockModel, VenteModel

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockModel
        fields = '__all__'


class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenteModel
        fields = '__all__'