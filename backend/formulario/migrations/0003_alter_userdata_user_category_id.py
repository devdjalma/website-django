# Generated by Django 5.1.4 on 2024-12-09 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0002_usercategory_userdata_user_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='user_category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='formulario.usercategory'),
        ),
    ]
