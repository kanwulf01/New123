# Generated by Django 2.2.3 on 2019-09-17 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_venta', '0004_factura2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura2',
            name='tienda',
        ),
        migrations.AddField(
            model_name='join2',
            name='facturax',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='join2', to='tienda_venta.Factura'),
        ),
    ]
