from django.contrib import admin
from models.ProblemasGastricos import ProblemasGastricos

@admin.register(ProblemasGastricos)
class ProblemasGastricosAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'name',
    )