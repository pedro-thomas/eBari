from django.contrib import admin
from consultas.models import FormBase, LocalRefeicao, QuemPrepara,TipoAlcool

class LocalRefeicaoAdmin(admin.ModelAdmin):
    icon_name='nature_people'
admin.site.register(LocalRefeicao,LocalRefeicaoAdmin)
class QuemPreparaAdmin(admin.ModelAdmin):
    icon_name='local_dining'
admin.site.register(QuemPrepara,QuemPreparaAdmin)

class TipoAlcoolAdmin(admin.ModelAdmin):
    icon_name='local_drink'
admin.site.register(TipoAlcool,TipoAlcoolAdmin)

class FormBaseAdmin(admin.ModelAdmin):
    list_display = ["consulta"]
    icon_name = 'description'
    
admin.site.register(FormBase, FormBaseAdmin)
