# Generated by Django 3.2.6 on 2021-09-02 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_alter_registrousuario_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrousuario',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='perfil/%Y/%m/%d'),
        ),
    ]
