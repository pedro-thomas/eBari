from django.contrib import admin
from consultas.models import FormBase, LocalRefeicao, QuemPrepara,TipoAlcool

admin.site.register(LocalRefeicao)
admin.site.register(QuemPrepara)
admin.site.register(TipoAlcool)

class FormBaseAdmin(admin.ModelAdmin):
    list_display = ["consulta"]
    icon_name = 'description'
    
admin.site.register(FormBase, FormBaseAdmin)