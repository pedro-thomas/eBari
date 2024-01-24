from django.contrib import admin
from models.TecnicaCirurgica import TecnicaCirurgica

@admin.register(TecnicaCirurgica)
class TecnicaCirurgicaAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'name',
    )