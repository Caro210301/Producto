# Generated by Django 5.1.2 on 2024-10-23 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0002_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principal',
            name='Categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miApp.categoria'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='Descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='principal',
            name='Oferta',
            field=models.BooleanField(default=False),
        ),
    ]
