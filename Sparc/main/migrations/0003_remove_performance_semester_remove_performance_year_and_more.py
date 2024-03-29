# Generated by Django 5.0.2 on 2024-02-22 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_customuser_semester_alter_customuser_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performance',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='year',
        ),
        migrations.AddField(
            model_name='unit',
            name='semester',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='course',
            field=models.ForeignKey(default='C025', on_delete=django.db.models.deletion.CASCADE, to='main.course'),
        ),
    ]
