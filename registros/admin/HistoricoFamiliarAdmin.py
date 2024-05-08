from django.contrib import admin
from registros.models import HistoricoFamiliar, OpcoesFamilia
@admin.register(OpcoesFamilia)
class OpcoesFamiliaAdmin(admin.ModelAdmin):
    list_display = ['name']
    icon_name='people'
@admin.register(HistoricoFamiliar)
class HistoricoFamiliarAdmin(admin.ModelAdmin):
    search_fields = ['patient',]
    list_display = ['patient',] 
    icon_name = 'assignment'