# Generated by Django 4.0.3 on 2022-03-25 17:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_newuser_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 25, 17, 26, 4, 551097, tzinfo=utc)),
        ),
    ]
