# Generated by Django 3.0.3 on 2020-08-25 15:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0012_auto_20200825_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the formet: '+999999999999'.up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
