from django.contrib import admin
from consultas.models import TipoDieta

class TipoDietaAdmin(admin.ModelAdmin):
    list_display = ["name"]
    icon_name = 'content_paste'

admin.site.register(TipoDieta,TipoDietaAdmin)