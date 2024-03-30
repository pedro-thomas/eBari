from django.contrib import admin
from consultas.models import FormBase

class FormBaseAdmin(admin.ModelAdmin):
    list_display = ["consulta"]
    icon_name = 'description'
    
admin.site.register(FormBase, FormBaseAdmin)