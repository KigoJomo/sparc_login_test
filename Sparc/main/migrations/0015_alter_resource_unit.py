# Generated by Django 5.0.2 on 2024-03-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_resource_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='unit',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
