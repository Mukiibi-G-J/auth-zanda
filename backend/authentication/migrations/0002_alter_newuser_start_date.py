# Generated by Django 4.0.3 on 2022-03-25 17:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 25, 17, 7, 48, 467659, tzinfo=utc)),
        ),
    ]
