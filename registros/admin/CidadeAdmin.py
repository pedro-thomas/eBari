from django.contrib import admin
from registros.models import Cidade

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    search_fields = (
        'name','state'
    )

    list_display = (
        'name','state'
    )