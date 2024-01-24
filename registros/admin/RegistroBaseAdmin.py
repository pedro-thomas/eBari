from django.contrib import admin
from models.RegistroBase import RegistroBase

@admin.register(RegistroBase)
class RegistroBaseAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'name',
    )