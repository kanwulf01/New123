# Generated by Django 2.2.3 on 2019-08-25 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_almacen', '0002_producto_categoria_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_almacen.Categoria'),
        ),
    ]
