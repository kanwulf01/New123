# Generated by Django 2.2.3 on 2019-07-30 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_venta', '0010_clienteoferta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('numero_oferta', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='clienteoferta',
            name='pedidoz',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='pedido',
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('numero_compra', models.AutoField(primary_key=True, serialize=False)),
                ('oferta', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tienda_venta.Oferta')),
            ],
        ),
        migrations.AddField(
            model_name='clienteoferta',
            name='ofertaz',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='tienda_venta.Oferta'),
        ),
        migrations.AddField(
            model_name='factura',
            name='comprax',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='tienda_venta.Compra'),
        ),
    ]