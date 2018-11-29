# Generated by Django 2.1.3 on 2018-11-15 23:21

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
            name='Mascota',
            fields=[
                ('codigoMascota', models.AutoField(primary_key=True, serialize=False)),
                ('fotoMascota', models.ImageField(blank=True, null=True, upload_to='media')),
                ('nombreMascota', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=20)),
                ('descripcion', models.TextField(default='Sin Descripcion', max_length=65)),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil', models.CharField(default='Invitado', max_length=20)),
                ('rutCliente', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
