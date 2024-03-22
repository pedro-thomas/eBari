from django.contrib import admin
from registros.models import Comorbidade

@admin.register(Comorbidade)
class ComorbidadesAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'name',
    )