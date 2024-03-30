from django.contrib import admin
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

admin.site.register(Consultas, ConsultasAdmin)