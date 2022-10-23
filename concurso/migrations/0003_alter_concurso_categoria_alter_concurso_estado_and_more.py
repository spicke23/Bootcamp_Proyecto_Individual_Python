# Generated by Django 4.0.2 on 2022-03-04 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concurso', '0002_alter_concurso_categoria_alter_receta_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concurso',
            name='categoria',
            field=models.IntegerField(choices=[[1, 'Desayunos'], [2, 'Almuerzos'], [3, 'Cenas'], [4, 'Snacks']]),
        ),
        migrations.AlterField(
            model_name='concurso',
            name='estado',
            field=models.IntegerField(choices=[[1, 'ACTIVO'], [2, 'INACTIVO']]),
        ),
        migrations.AlterField(
            model_name='receta',
            name='categoria',
            field=models.IntegerField(choices=[[1, 'Desayunos'], [2, 'Almuerzos'], [3, 'Cenas'], [4, 'Snacks']]),
        ),
    ]