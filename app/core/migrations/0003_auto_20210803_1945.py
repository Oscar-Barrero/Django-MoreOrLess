# Generated by Django 3.2.5 on 2021-08-04 00:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210803_1601'),
    ]

    operations = [
        migrations.DeleteModel(
            name='presupuesto',
        ),
        migrations.AddField(
            model_name='metas',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='metas',
            name='f_c_m',
            field=models.DateField(verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2021, 8, 3, 19, 45, 12, 596224), verbose_name='Fecha de registro'),
        ),
    ]
