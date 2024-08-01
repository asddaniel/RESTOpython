from django.contrib import admin
from .models import StockModel, VenteModel

# Register your models here.

admin.site.register(StockModel)
admin.site.register(VenteModel)