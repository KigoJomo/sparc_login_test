# Generated by Django 5.0.2 on 2024-03-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_resource_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='file_attachment',
            field=models.FileField(upload_to='resource_attachments'),
        ),
    ]
