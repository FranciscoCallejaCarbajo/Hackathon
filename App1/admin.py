from django.contrib import admin
from .models import Usuarios

admin.site.site_header = 'Usuarios'
admin.site.site_title = 'Usuario'
# Register your models here.
@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    fields = ["nombre", "apellido", "email", "contraseña", "birthday"]
    list_display = ["nombre", "apellido", "email", "contraseña", "birthday"]

