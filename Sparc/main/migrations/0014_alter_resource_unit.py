# Generated by Django 5.0.2 on 2024-03-04 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_resource_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.unit'),
        ),
    ]
