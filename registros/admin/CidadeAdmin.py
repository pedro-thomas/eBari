from django.contrib import admin
from models.Cidade import Cidade

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'name',
    )