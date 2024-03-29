from django.contrib import admin
from registros.models import TecnicaCirurgica

@admin.register(TecnicaCirurgica)
class TecnicaCirurgicaAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    icon_name = 'local_hospital'