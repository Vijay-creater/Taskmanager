# Generated by Django 4.1.13 on 2024-06-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_rename_status_taskstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]
