# Generated by Django 5.1.2 on 2024-10-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Precio', models.IntegerField()),
                ('Categoria', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=50)),
                ('Stock', models.IntegerField()),
                ('Unidades_Vendidas', models.IntegerField()),
                ('Oferta', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
