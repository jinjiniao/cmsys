# Generated by Django 2.2.6 on 2019-11-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_auto_20191103_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, verbose_name='姓名'),
        ),
    ]
