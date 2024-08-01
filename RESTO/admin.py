from django.contrib import admin
from .models import Plat, PlatCategorie, Commandes, CommandItems, Boisson, BoissonCategorie


admin.site.register(Plat)
admin.site.register(Boisson)
admin.site.register(PlatCategorie)
admin.site.register(BoissonCategorie)
admin.site.register(Commandes)
admin.site.register(CommandItems)
