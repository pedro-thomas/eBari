from django.contrib import admin
from models.Medicos import Medicos

@admin.register(Medicos)
class MedicosAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'name',
    )