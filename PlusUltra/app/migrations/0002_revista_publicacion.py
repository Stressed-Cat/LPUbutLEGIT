# Generated by Django 4.0.4 on 2022-05-12 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('fecha', models.DateField()),
                ('investigador', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('revista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.revista')),
            ],
        ),
    ]
