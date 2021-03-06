# Generated by Django 2.2.3 on 2019-08-17 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id_tienda', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_tienda', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('tienda_lider', models.IntegerField()),
                ('ingreso', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='suscripcion',
            fields=[
                ('id_suscripcion', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('puntos_tienda', models.IntegerField()),
                ('comision_pago', models.IntegerField()),
                ('tienda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda_suscripcion.Tienda')),
            ],
        ),
    ]
