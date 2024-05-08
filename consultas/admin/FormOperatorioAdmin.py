from django.contrib import admin
from consultas.models import PosOperatorio, PreOperatorio, OrientacaoDieta, CausaGanhoPeso, Complicacoes

class OrientacaoDietaAdmin(admin.ModelAdmin):
  icon_name='record_voice_over'
admin.site.register(OrientacaoDieta,OrientacaoDietaAdmin)
class ComplicacoesAdmin(admin.ModelAdmin):
  icon_name='mood_bad'
admin.site.register(Complicacoes,ComplicacoesAdmin)

class CausaGanhoPesoAdmin(admin.ModelAdmin):
    icon_name='timeline'
admin.site.register(CausaGanhoPeso,CausaGanhoPesoAdmin)

class PreOperatorioAdmin(admin.ModelAdmin):
    list_display = ["consulta"]
    icon_name = 'first_page'

admin.site.register(PreOperatorio, PreOperatorioAdmin)

class PosOperatorioAdmin(admin.ModelAdmin):
    list_display = ["consulta"]
    icon_name = 'last_page'
    
admin.site.register(PosOperatorio, PosOperatorioAdmin)