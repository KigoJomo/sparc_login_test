# Generated by Django 5.0.2 on 2024-03-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_customuser_streak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateField(),
        ),
    ]