from django.contrib import admin
from consultas.models import PosOperatorio, PreOperatorio

class PreOperatorioAdmin(admin.ModelAdmin):
    list_display = ["consulta"]
    icon_name = 'first_page'

admin.site.register(PreOperatorio, PreOperatorioAdmin)

class PosOperatorioAdmin(admin.ModelAdmin):
    list_display = ["consulta"]
    icon_name = 'last_page'
    
admin.site.register(PosOperatorio, PosOperatorioAdmin)