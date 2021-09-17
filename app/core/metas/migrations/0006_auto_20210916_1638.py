# Generated by Django 3.2.6 on 2021-09-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0005_alter_metas_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='metas',
            name='porcentaje',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Porcentaje'),
        ),
        migrations.AlterField(
            model_name='metas',
            name='amount',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Monto'),
        ),
    ]