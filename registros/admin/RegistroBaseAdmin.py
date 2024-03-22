from django.contrib import admin
from registros.models import RegistroBase

@admin.register(RegistroBase)
class RegistroBaseAdmin(admin.ModelAdmin):
    search_fields = [
        'type',
    ]

    list_display = [
        'type',
    ]