# Generated by Django 5.0.2 on 2024-03-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_session_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]