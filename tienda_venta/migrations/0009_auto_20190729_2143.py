# Generated by Django 2.2.3 on 2019-07-29 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_venta', '0008_auto_20190726_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente2',
            name='contra',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente2',
            name='email',
            field=models.EmailField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente2',
            name='lastname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente2',
            name='nombre',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente2',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]