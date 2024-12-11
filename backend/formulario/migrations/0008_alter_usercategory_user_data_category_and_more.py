# Generated by Django 5.1.4 on 2024-12-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0007_userdata_data_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercategory',
            name='user_data_category',
            field=models.CharField(choices=[('Engenheiro', 'Engenheiro'), ('Estudante', 'Estudante'), ('Professor', 'Professor'), ('Programador', 'Programador'), ('Outro', 'Outro')], max_length=100),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='grau_ensino',
            field=models.CharField(choices=[('Ensino Médio Completo', 'Ensino Médio Completo'), ('Ensino Superior Completo', 'Ensino Superior Completo'), ('Mestre', 'Mestre'), ('Doutor', 'Doutor'), ('Einsten', 'Einsten'), ('Oppenheimer', 'Oppenheimer')], default='Não informado', max_length=100),
        ),
    ]
