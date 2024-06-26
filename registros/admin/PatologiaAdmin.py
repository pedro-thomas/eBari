from django.contrib import admin
from registros.models import Patologia

@admin.register(Patologia)
class PatologiaAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    icon_name='accessibility_new'