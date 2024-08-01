from rest_framework import serializers
from .models import Plat, BoissonCategorie, Boisson, PlatCategorie, Commandes, CommandItems

class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = '__all__'


class BoissonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boisson
        fields = '__all__'

class BoissonCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoissonCategorie
        fields = '__all__'

class PlatCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatCategorie
        fields = '__all__'

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commandes
        fields = '__all__'

class CommandItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandItems
        fields = '__all__'