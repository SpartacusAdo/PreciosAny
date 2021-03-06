# Generated by Django 4.0.4 on 2022-05-16 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=25, unique=True)),
                ('slug', models.SlugField(max_length=255)),
                ('orden', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['categoria'],
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ['color'],
            },
        ),
    ]
