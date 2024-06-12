from django.contrib import admin
from .models import Usuarios, Categoria, Curso, UsuarioCurso, CursoCategoria

admin.site.site_header = 'Usuarios'
admin.site.site_title = 'Usuario'
# Register your models here.
@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    fields = ["nombre", "apellido", "email", "contraseña", "birthday"]
    list_display = ["nombre", "apellido", "email", "contraseña", "birthday"]

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion', 'precio', 'valoracion', 'enlace', 'imagen']
    search_fields = ['titulo', 'descripcion']
    list_filter = ['categorias']

@admin.register(UsuarioCurso)
class UsuarioCursoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'curso']
    search_fields = ['usuario__username', 'curso__titulo']

@admin.register(CursoCategoria)
class CursoCategoriaAdmin(admin.ModelAdmin):
    list_display = ['curso', 'categoria']
    search_fields = ['curso__titulo', 'categoria__nombre']