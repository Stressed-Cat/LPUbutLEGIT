# Generated by Django 4.0.5 on 2022-06-06 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_ciudad_editorial_tipo_articulo_idioma_usuario_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Email',
            field=models.EmailField(default='a', max_length=254, unique=True, verbose_name='Email address'),
            preserve_default=False,
        ),
    ]
