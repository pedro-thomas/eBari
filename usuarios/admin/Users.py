from django.contrib import admin
from usuarios.models import User as Usuarios
from django.contrib.auth.models import Group

# admin.site.unregister(Group)
@admin.register(Usuarios)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)

    icon_name='account_circle'