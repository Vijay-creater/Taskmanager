# Generated by Django 4.1.13 on 2024-01-30 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Status',
            new_name='TaskStatus',
        ),
    ]
