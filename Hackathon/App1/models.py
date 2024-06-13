from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre", null=False, blank=False)
    apellido = models.CharField(max_length=50, verbose_name="Apellido", null=False, blank=False)
    email = models.EmailField(max_length=50, verbose_name="Email", null=False, blank=False)
    contraseña = models.CharField(max_length=50, verbose_name="Contraseña", null=False, blank=False)
    birthday = models.DateField(null=False, verbose_name="Cumpleaños", blank=False)

    class Meta:
        db_table = "Usuarios"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def _str_(self) -> str:
        return self.nombre
    
# Modelo de Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre")

    class Meta:
        db_table = "Categorias"
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre

# Modelo de Curso
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

# Modelo de Relación Curso-Categoría
class CursoCategoria(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        db_table = "CursoCategoria"
        verbose_name = "Curso-Categoría"
        verbose_name_plural = "Cursos-Categorías"
        unique_together = ('curso', 'categoria')

# Modelo de Relación Usuario-Curso
class UsuarioCurso(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        db_table = "UsuarioCurso"
        verbose_name = "Usuario-Curso"
        verbose_name_plural = "Usuarios-Cursos"
        unique_together = ('usuario', 'curso')