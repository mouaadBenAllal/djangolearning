from django.contrib import admin
from .models import Auto


class AutoAdmin(admin.ModelAdmin):

    model = Auto
    list_display = ('merk_auto', 'type_auto', 'brandstof', 'kleur', 'bouwjaar','prijs')

admin.site.register(Auto,AutoAdmin)




































