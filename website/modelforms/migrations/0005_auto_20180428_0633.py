# Generated by Django 2.0.4 on 2018-04-28 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelforms', '0004_auto_20180428_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_horsepower',
            field=models.IntegerField(),
        ),
    ]
