# Generated by Django 3.2.8 on 2023-05-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('contrasena', models.TextField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Contacto',
        ),
    ]
