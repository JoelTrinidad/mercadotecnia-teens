# Generated by Django 2.0.2 on 2018-11-18 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20181115_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='precio'),
        ),
    ]