# Generated by Django 3.2.6 on 2021-09-30 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gastos', '0021_gastos_week'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gastos',
            name='week',
        ),
    ]
