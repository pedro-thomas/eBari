from django.contrib import admin
from django.utils.html import format_html

from consultas.models import Consultas
from consultas.models import PosOperatorio, PreOperatorio
from consultas.models import Exames

class PreOperatorioInline(admin.StackedInline):
    model = PreOperatorio
    extra = 0

class PosOperatorioInline(admin.StackedInline):
    model = PosOperatorio
    extra = 0

class ExameInline(admin.StackedInline):
    model = Exames
    extra = 0

class ConsultasAdmin(admin.ModelAdmin):
    model = Consultas
    list_display = ["paciente", "date", "type"]
    icon_name = 'perm_contact_calendar'
    inlines = (
        PreOperatorioInline,
        PosOperatorioInline,
        ExameInline,
    )
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj=obj)
        # Adicione o estilo CSS diretamente no HTML usando format_html
        fieldsets_html = format_html('<style>.card-grid{{ display: block; }}</style>')
        fieldsets = list(fieldsets)  # Converta para lista para poder modificar
        fieldsets.append(('', {'fields': [], 'description': fieldsets_html}))
        return fieldsets

admin.site.register(Consultas, ConsultasAdmin)