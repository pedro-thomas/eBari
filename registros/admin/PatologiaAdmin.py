from django.contrib import admin
from models.Patologia import Patologia

@admin.register(Patologia)
class PatologiaAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'name',
    )