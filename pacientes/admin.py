from django.contrib import admin
# from evolutions.models import Evolution
# from nutritional_consultations.models import NutritionalConsultation
from import_export.admin import ImportExportModelAdmin
# from registers.models import HistoricoFamiliar
from .models import Paciente, Contato
from django.contrib import admin


class ContatoInline(admin.TabularInline):
    model = Contato
    extra = 0

# class HistoricoFamiliarInline(admin.StackedInline):
#     model = HistoricoFamiliar
#     extra = 0

@admin.register(Paciente)
class PacienteAdmin(ImportExportModelAdmin):

    search_fields = (
        'full_name',
        'cpf',
    )

    list_display = (
        'full_name',
        'cpf',
        'gender',
        'birth_date',
        'address_city',
        'age',
    )

    autocomplete_fields = (
        'address_city',
    )

    list_filter = (
        'address_city',
        'gender',
    )

    inlines = (
        # HistoricoFamiliarInline,
        ContatoInline
    )

    def age(self, obj):
        return obj.age() 
    age.short_description = 'Idade'
    
# @admin.register(HistoricoFamiliar)
# class HistoricoFamiliarAdmin(admin.ModelAdmin):
#     search_fields = (
#         'paciente__full_name',
#         'paciente__cpf',
#     )

#     list_display = (
#         'paciente',
#         'created_at',
#         'updated_at',
#     )

#     autocomplete_fields = (
#         'paciente',
#     )