from django.contrib import admin
from registros.models import HistoricoFamiliar

@admin.register(HistoricoFamiliar)
class HistoricoFamiliarAdmin(admin.ModelAdmin):
    search_fields = [
        'patient',
    ]

    list_display = [
        'patient',
    ]