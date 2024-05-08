from django.contrib import admin
from registros.models import Suplemento

@admin.register(Suplemento)
class SuplementoAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    icon_name = 'local_pharmacy'