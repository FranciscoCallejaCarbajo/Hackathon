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