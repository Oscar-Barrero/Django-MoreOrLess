# Generated by Django 3.2.6 on 2021-09-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0008_remove_informes_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='informes',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de registro'),
        ),
    ]
