# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0005_auto_20161216_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='image',
            field=models.FileField(default=False, upload_to='autoimages/'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='brandstof',
            field=models.CharField(choices=[('Benzine', 'Benzine'), ('Diesel', 'Diesel'), ('Lpg', 'Lpg'), ('Elektrisch', 'Elektrisch'), ('Hybrid', 'Hybrid')], max_length=50),
        ),
        migrations.AlterField(
            model_name='auto',
            name='kleur',
            field=models.CharField(choices=[('Zwart', 'Zwart'), ('Blauw', 'Blauw'), ('Grijs', 'Grijs'), ('Wit', 'Wit'), ('Groen', 'Groen'), ('Geel', 'Geel'), ('Roze', 'Roze')], default='Zwart', max_length=50),
        ),
        migrations.AlterField(
            model_name='auto',
            name='merk_auto',
            field=models.CharField(choices=[('Audi', 'Audi'), ('Bmw', 'Bmw'), ('Mercedes', 'Mercedes'), ('Opel', 'Opel'), ('Citroen', 'Citroen')], max_length=9),
        ),
        migrations.AlterField(
            model_name='auto',
            name='type_auto',
            field=models.CharField(choices=[('Audi', (('a1', 'A1'), ('a3', 'A3'), ('a4', 'A4'), ('a5', 'A5'), ('a6', 'A6'))), ('Bmw', (('1-serie', '1-serie'), ('3-serie', '3-serie'), ('5-serie', '5-serie'), ('6-serie', '6-serie'))), ('Mercedes', (('A-klasse', 'A-klasse'), ('B-klasse', 'B-klasse'), ('C-klasse', 'C-klasse'), ('E-klasse', 'E-klasse'), ('S-klasse', 'S-klasse'))), ('Citroen', (('c1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C4'), ('C5', 'C5'))), ('Opel', (('Corsa', 'Corsa'), ('Zafira', 'Zafira'), ('Karl', 'Karl'), ('Astra', 'Astra'), ('Insignia', 'Insignia')))], max_length=50),
        ),
    ]