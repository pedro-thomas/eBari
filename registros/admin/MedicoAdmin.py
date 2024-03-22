from django.contrib import admin
from registros.models import Medico

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'name',
    )