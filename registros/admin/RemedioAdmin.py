from django.contrib import admin
from models.Remedio import Remedio

@admin.register(Remedio)
class RemedioAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'name',
    )