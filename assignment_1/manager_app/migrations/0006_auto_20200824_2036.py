# Generated by Django 3.0.6 on 2020-08-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0005_auto_20200824_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateTimeField(null=True),
        ),
    ]
