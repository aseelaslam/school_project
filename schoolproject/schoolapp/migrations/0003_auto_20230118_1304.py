# Generated by Django 3.2.15 on 2023-01-18 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0002_auto_20230118_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='district',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='branch',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='district',
            new_name='department',
        ),
    ]
