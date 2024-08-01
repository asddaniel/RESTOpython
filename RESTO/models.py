from django.db import models

# Create your models here.

class Plat(models.Model):
    name = models.CharField(max_length = 255, unique=True)
    prix = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    platcategorie_id = models.CharField(max_length=255)
    prix_vip = models.FloatField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    special_id = models.CharField(max_length=255, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
class Boisson(models.Model):
    name = models.CharField(max_length = 255, unique=True)
    prix = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    boissoncategorie_id = models.CharField(max_length=255)
    prix_vip = models.FloatField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    special_id = models.CharField(max_length=255, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Commandes(models.Model):
    client = models.CharField(max_length = 255, unique=False, blank=True)
    reduction = models.FloatField(null=True, blank=True)
    prix_vip = models.FloatField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    special_id = models.CharField(max_length=255, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

class CommandItems(models.Model):
    description = models.CharField(max_length = 255, null=True, blank=True)
    quantite = models.IntegerField(default=0)
    command_id = models.CharField(max_length = 255, null=True)
    plat_id = models.CharField(max_length = 255, null=True)
    montant = models.FloatField(default=0)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    special_id = models.CharField(max_length=255, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']



class PlatCategorie(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    special_id = models.CharField(max_length=255, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

class BoissonCategorie(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    special_id = models.CharField(max_length=255, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

