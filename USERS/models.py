from django.db import models
from django.contrib.auth.models import User

# Élargissons les choix possibles pour le poste
service = (
    ('ADMINISTRATEUR', 'ADMINISTRATEUR'),
    ('UTILISATEUR', 'UTILISATEUR'),
    ('MANAGER', 'MANAGER'),
    ('SERVEUR', 'SERVEUR')
)

class Poste(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    poste = models.CharField(max_length=50, choices=service, verbose_name='catégorie utilisateur')

    class Meta:
        verbose_name = 'utilisateur'

    def __str__(self):
        return str(self.user)
