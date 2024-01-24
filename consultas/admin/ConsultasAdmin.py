from django.contrib import admin
from models.Consultas import Consulta
from models.FormOperatorio import PosOperatorio, PreOperatorio
from models.Exames import Exame

class PreOperatorioInline(admin.StackedInline):
    model = PreOperatorio
    extra = 0

class PosOperatorioInline(admin.StackedInline):
    model = PosOperatorio
    extra = 0

class ExameInline(admin.StackedInline):
    model = Exame
    extra = 0

class ConsultasAdmin(admin.ModelAdmin):
    list_display = ["patient", "date", "type"]

    inlines = (
        PreOperatorioInline,
        PosOperatorioInline,
        ExameInline,
    )

admin.site.register(Consulta, ConsultasAdmin)