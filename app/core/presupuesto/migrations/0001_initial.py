# Generated by Django 3.2.5 on 2021-08-04 00:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Monto')),
                ('category', models.CharField(max_length=50, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Presupuesto',
                'verbose_name_plural': 'Presupuestos',
                'db_table': 'presupuesto',
                'ordering': ['id'],
            },
        ),
    ]
