from django.contrib import admin
from registros.models import ProblemasGastricos

@admin.register(ProblemasGastricos)
class ProblemasGastricosAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    icon_name = 'sentiment_very_dissatisfied'