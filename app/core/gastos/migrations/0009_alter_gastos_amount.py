# Generated by Django 3.2.5 on 2021-08-10 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gastos', '0008_alter_gastos_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastos',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Monto'),
        ),
    ]
