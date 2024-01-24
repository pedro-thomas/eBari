from django.contrib import admin
from models.FormOperatorio import PosOperatorio, PreOperatorio

class PreOperatorioAdmin(admin.ModelAdmin):
    list_display = ["consulta"]

admin.site.register(PreOperatorio, PreOperatorioAdmin)

class PosOperatorioAdmin(admin.ModelAdmin):
    list_display = ["consulta"]

admin.site.register(PosOperatorio, PosOperatorioAdmin)