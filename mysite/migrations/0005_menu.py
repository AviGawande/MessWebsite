# Generated by Django 4.1.7 on 2023-03-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_rename_name_customer_fname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(max_length=255)),
                ('f2', models.CharField(max_length=255)),
                ('f3', models.CharField(max_length=255)),
                ('f4', models.CharField(max_length=255)),
                ('f5', models.CharField(max_length=255)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
