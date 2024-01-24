from django.contrib import admin
from models.HistoricoFamiliar import HistoricoFamiliar

@admin.register(HistoricoFamiliar)
class HistoricoFamiliarAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'name',
    )