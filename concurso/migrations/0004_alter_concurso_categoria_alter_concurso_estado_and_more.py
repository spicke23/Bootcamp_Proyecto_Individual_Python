# Generated by Django 4.0.2 on 2022-03-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concurso', '0003_alter_concurso_categoria_alter_concurso_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concurso',
            name='categoria',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='concurso',
            name='estado',
            field=models.IntegerField(choices=[['ACTIVO', 'ACTIVO'], ['INACTIVO', 'INACTIVO']]),
        ),
        migrations.AlterField(
            model_name='concurso',
            name='fecha_inicio',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='concurso',
            name='fecha_termino',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='categoria',
            field=models.CharField(max_length=15),
        ),
    ]
