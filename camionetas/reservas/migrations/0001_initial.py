# Generated by Django 4.1.4 on 2022-12-06 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('apellido_paterno', models.CharField(blank=True, max_length=20, null=True)),
                ('apellido_materno', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id_vehiculo', models.AutoField(db_column='id_vehiculo', primary_key=True, serialize=False)),
                ('patente', models.CharField(blank=True, max_length=10, null=True)),
                ('marca', models.CharField(blank=True, max_length=20, null=True)),
                ('modelo', models.CharField(blank=True, max_length=20, null=True)),
                ('anio', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]