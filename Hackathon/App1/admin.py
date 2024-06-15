from django.contrib import admin
from .models import Usuarios, Categoria, Curso, UsuarioCurso, CursoCategoria, Favoritos

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    fields = ["nombre", "apellido", "email", "contraseña", "birthday"]
    list_display = ["nombre", "apellido", "email", "birthday"]
    search_fields = ["nombre", "apellido", "email"]

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
    search_fields = ['usuario__user__username', 'curso__titulo']

@admin.register(CursoCategoria)
class CursoCategoriaAdmin(admin.ModelAdmin):
    list_display = ['curso', 'categoria']
    search_fields = ['curso__titulo', 'categoria__nombre']

@admin.register(Favoritos)
class FavoritosAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'curso', 'fecha']
    search_fields = ['usuario__nombre', 'curso__titulo']
