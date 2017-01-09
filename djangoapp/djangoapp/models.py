from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from djmoney.models.fields import MoneyField


# Create your models here.


class Auto(models.Model):

    AUD = "Audi"
    BMW = "Bmw"
    MER = "Mercedes"
    VOL = "Volvo"
    VW = "Volkswagen"
    OP = "Opel"
    SUZ = "Suzuki"
    CIT = "Citroen"
    PEU = "Peugeot"
    AUTO_CHOICES = (
        (AUD, "Audi"),
        (BMW, "Bmw"),
        (MER, "Mercedes"),
        (OP, "Opel"),
        (CIT, "Citroen"),
    )

    ZWART = "Zwart"
    BLAUW = "Blauw"
    GRIJS = "Grijs"
    WIT = "Wit"
    GROEN = "Groen"
    GEEL = "Geel"
    ROZE = "Roze"
    KLEUR_CHOICES = (
        (ZWART, "Zwart"),
        (BLAUW, "Blauw"),
        (GRIJS, "Grijs"),
        (WIT, "Wit"),
        (GROEN, "Groen"),
        (GEEL, "Geel"),
        (ROZE, "Roze"),
        (ROZE, "Rood"),
    )

    BEN = "Benzine"
    DIE = "Diesel"
    LPG = "Lpg"
    ELE = "Elektrisch"
    HYB = "Hybrid"
    BRANDSTOF_CHOICES = (
        (BEN, "Benzine"),
        (DIE, "Diesel"),
        (LPG, "Lpg"),
        (ELE, "Elektrisch"),
        (HYB, "Hybrid"),
    )

    TYPE_CHOICES = (
        ('Audi', (
            ('a1', 'A1'),
            ('a3', 'A3'),
            ('a4', 'A4'),
            ('a5', 'A5'),
            ('a6', 'A6'),
        )
         ),
        ('Bmw', (
            ('1-serie', '1-serie'),
            ('3-serie', '3-serie'),
            ('5-serie', '5-serie'),
            ('6-serie', '6-serie'),
        )
         ),
        ('Mercedes', (
            ('A-klasse', 'A-klasse'),
            ('B-klasse', 'B-klasse'),
            ('C-klasse', 'C-klasse'),
            ('E-klasse', 'E-klasse'),
            ('S-klasse', 'S-klasse'),
        )
         ),
        ('Citroen', (
            ('c1', 'C1'),
            ('C2', 'C2'),
            ('C3', 'C3'),
            ('C4', 'C4'),
            ('C5', 'C5'),
        )
         ),
        ('Opel', (
            ('Corsa', 'Corsa'),
            ('Zafira', 'Zafira'),
            ('Karl', 'Karl'),
            ('Astra', 'Astra'),
            ('Insignia', 'Insignia'),
        )
         ),
    )

    merk_auto = models.CharField(max_length=9, choices=AUTO_CHOICES)
    type_auto = models.CharField(max_length=50,choices=TYPE_CHOICES)
    brandstof = models.CharField(max_length=50,choices=BRANDSTOF_CHOICES)
    kleur = models.CharField(max_length=50, choices=KLEUR_CHOICES, default=ZWART)
    bouwjaar = models.IntegerField()
    prijs = MoneyField(decimal_places=2, default=0, default_currency='EUR', max_digits=11,)
    image = models.ImageField(upload_to='autoimages/', default=False)

    def __str__(self):
        return self.merk_auto

