# Generated by Django 5.0.7 on 2024-07-29 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RESTO', '0003_rename_commande_id_commanditems_command_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandes',
            name='client',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
