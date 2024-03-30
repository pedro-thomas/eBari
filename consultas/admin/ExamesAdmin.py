from django.contrib import admin
from consultas.models import Exames

class ExamesAdmin(admin.ModelAdmin):
    list_display = ["consulta"]
    icon_name = 'content_paste'

admin.site.register(Exames,ExamesAdmin)