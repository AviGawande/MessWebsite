# Generated by Django 4.1.7 on 2023-04-19 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_attendance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='Date',
            new_name='date_in',
        ),
    ]
