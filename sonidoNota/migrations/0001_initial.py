# Generated by Django 3.1.3 on 2024-06-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SonidoNota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(max_length=5)),
                ('instrumento', models.CharField(max_length=100)),
                ('sonido_url', models.URLField()),
            ],
        ),
    ]