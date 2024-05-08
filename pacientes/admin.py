from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from pacientes.models import Paciente, Contato, HorarioTrabalho

# from evolutions.models import Evolution
# from nutritional_consultations.models import NutritionalConsultation
# from registros.models import HistoricoFamiliar


class ContatoInline(admin.TabularInline):
    model = Contato
    extra = 0

@admin.register(HorarioTrabalho)
class HorarioTrabalhoAdmin(admin.ModelAdmin):
    model = HorarioTrabalho
    icon_name='access_time'
    extra = 0

@admin.register(Paciente)

class PacienteAdmin(admin.ModelAdmin):
    icon_name = 'account_box'
    search_fields = ('full_name','cpf',)
    list_display = ('full_name','cpf','gender','birth_date','address_city','age',)
    autocomplete_fields = ('address_city',)

    inlines = [
        ContatoInline
    ]

    def age(self, obj):
        return obj.age() 
    age.short_description = 'Idade'