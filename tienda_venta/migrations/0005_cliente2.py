# Generated by Django 2.2.3 on 2019-07-21 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_venta', '0004_auto_20190716_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente2',
            fields=[
                ('cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('seller', models.BooleanField(default=False)),
                ('contra', models.CharField(max_length=20)),
            ],
        ),
    ]