from django.db import models
from django.contrib.auth.models import User

class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    email = models.EmailField(max_length=50, verbose_name="Email", unique=True)
    birthday = models.DateField(verbose_name="Cumpleaños")
    favoritos = models.ManyToManyField('Curso', through='Favoritos', related_name='usuarios_favoritos')

    class Meta:
        db_table = "Usuarios"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre")

    class Meta:
        db_table = "Categorias"
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    valoracion = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Valoración")
    enlace = models.URLField(max_length=255, verbose_name="Enlace")
    imagen = models.ImageField(upload_to='cursos/', verbose_name="Imagen")
    categorias = models.ManyToManyField(Categoria, through='CursoCategoria', related_name='cursos')
    usuarios = models.ManyToManyField(Usuarios, through='UsuarioCurso', related_name='cursos_inscritos')

    class Meta:
        db_table = "Cursos"
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.titulo

class CursoCategoria(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        db_table = "CursoCategoria"
        verbose_name = "Curso-Categoría"
        verbose_name_plural = "Cursos-Categorías"
        unique_together = ('curso', 'categoria')

    def __str__(self):
        return f"{self.curso.titulo} - {self.categoria.nombre}"

class UsuarioCurso(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        db_table = "UsuarioCurso"
        verbose_name = "Usuario-Curso"
        verbose_name_plural = "Usuarios-Cursos"
        unique_together = ('usuario', 'curso')

    def __str__(self):
        return f"{self.usuario.nombre} {self.usuario.apellido} - {self.curso.titulo}"

class Favoritos(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='favoritos_relacionados')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Favoritos"
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"
        unique_together = ('usuario', 'curso')

    def __str__(self):
        return f"{self.usuario.nombre} {self.usuario.apellido} - {self.curso.titulo}"
