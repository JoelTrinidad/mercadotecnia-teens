# Generated by Django 2.0.2 on 2018-11-15 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20181115_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Nombre')),
                ('image', models.ImageField(upload_to='products', verbose_name='Imagen')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Imagen2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Imagen3')),
                ('price', models.FloatField(verbose_name='precio')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de cración')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]