# Generated by Django 4.1.7 on 2023-04-20 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=120)),
                ('year', models.CharField(max_length=50)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]