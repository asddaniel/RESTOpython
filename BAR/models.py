from django.db import models

# Create your models here.

class StockModel(models.Model):
    boison = models.CharField(max_length = 100, unique=True)
    quantite = models.IntegerField(default = 0)
    prix = models.FloatField()
    date_stock = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-date_stock']

    def __str__(self):
        return self.boison
    
class VenteModel(models.Model):
    client = models.CharField(max_length = 100)
    vente_boison = models.ManyToManyField(StockModel)
    nombre = models.PositiveIntegerField(default = 1)
    delete_alt = models.BooleanField(default = True)
    date_vente = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-date_vente']

    def __str__(self):
        return self.client


