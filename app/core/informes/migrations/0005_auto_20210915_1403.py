# Generated by Django 3.2.6 on 2021-09-15 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gastos', '0014_merge_20210908_1119'),
        ('informes', '0004_remove_informes_restante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informes',
            name='presupuesto',
        ),
        migrations.AlterField(
            model_name='informes',
            name='gastos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gastos.gastos'),
        ),
    ]