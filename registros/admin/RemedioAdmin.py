from django.contrib import admin
from registros.models import Remedio

@admin.register(Remedio)
class RemedioAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    icon_name = 'local_pharmacy'