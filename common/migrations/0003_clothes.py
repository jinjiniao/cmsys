# Generated by Django 2.2.6 on 2019-10-25 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20191025_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sn', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
    ]
