# Generated by Django 2.2.3 on 2019-09-17 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_almacen', '0009_auto_20190913_0035'),
        ('tienda_venta', '0002_pago'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_venta.Pedido')),
                ('producto1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_almacen.Producto')),
                ('vendedor1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_venta.Cliente2')),
            ],
        ),
    ]
