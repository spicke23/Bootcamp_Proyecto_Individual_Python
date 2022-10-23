# Generated by Django 4.0.2 on 2022-03-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('categoria', models.IntegerField(choices=[[0, 'Consulta'], [1, 'Reclamo'], [2, 'Felicitaciones'], [3, 'Sugerencias']])),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
    ]
