from django.contrib import admin
from models.FormBase import FormBase

class FormBaseAdmin(admin.ModelAdmin):
    list_display = ["consulta"]

admin.site.register(FormBase, FormBaseAdmin)