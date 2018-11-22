from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de cración")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edición")
    
    class Meta:
            verbose_name="Pregunta"
            verbose_name_plural="Preguntas"
            ordering = ["-created"]
    def __str__(self):
        return self.title