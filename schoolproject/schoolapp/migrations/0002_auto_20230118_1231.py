# Generated by Django 3.2.15 on 2023-01-18 07:01

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Branch',
            new_name='Course',
        ),
        migrations.RenameModel(
            old_name='District',
            new_name='Department',
        ),
    ]
