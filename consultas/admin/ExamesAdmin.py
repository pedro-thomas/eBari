from django.contrib import admin
from consultas.models import Exames

admin.site.register(Exames)
class ExamesAdmin(admin.ModelAdmin):
    list_display = ["consulta"]
