# Generated by Django 2.2.16 on 2020-10-20 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto6', '0003_auto_20201020_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insumos',
            old_name='descripsion',
            new_name='descripcion',
        ),
    ]