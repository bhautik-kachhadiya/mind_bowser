# Generated by Django 3.0.6 on 2020-08-24 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0004_auto_20200824_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]