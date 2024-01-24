from django.contrib import admin
from models.Exames import Exame

class ExameAdmin(admin.ModelAdmin):
    list_display = ["consultation"]

admin.site.register(Exame, ExameAdmin)