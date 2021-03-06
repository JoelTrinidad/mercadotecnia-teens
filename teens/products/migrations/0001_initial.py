# Generated by Django 2.0.2 on 2018-11-15 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('image', models.ImageField(upload_to='products', verbose_name='Imagen')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Imagen2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Imagen3')),
                ('price', models.FloatField(verbose_name='precio')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
        ),
    ]
