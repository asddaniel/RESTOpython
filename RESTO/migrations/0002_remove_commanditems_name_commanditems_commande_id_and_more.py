# Generated by Django 5.0.7 on 2024-07-29 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RESTO', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commanditems',
            name='name',
        ),
        migrations.AddField(
            model_name='commanditems',
            name='commande_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='commanditems',
            name='plat_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
