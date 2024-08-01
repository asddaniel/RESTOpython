# Generated by Django 4.2.7 on 2024-02-16 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poste', models.CharField(choices=[('ADMINISTRATEUR', 'ADMINISTRATEUR'), ('UTILISATEUR', 'UTILISATEUR')], max_length=50, verbose_name='categorie utilisateur')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'utilisateur',
            },
        ),
    ]
