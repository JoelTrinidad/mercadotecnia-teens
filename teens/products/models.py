from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=400, verbose_name="Nombre")
    image = models.ImageField(verbose_name="Imagen", upload_to= "products")
    image2 = models.ImageField(verbose_name="Imagen2", upload_to= "products", blank=True, null=True)
    image3 = models.ImageField(verbose_name="Imagen3", upload_to= "products", blank=True, null=True)
    price = models.FloatField(verbose_name="precio", default=0.00)
    description = models.TextField(verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de cración")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edición")

    class Meta:
            verbose_name="Producto"
            verbose_name_plural="Productos"
            ordering = ["-created"]
    def __str__(self):
        return self.name
    