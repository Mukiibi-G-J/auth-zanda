# Generated by Django 4.0.3 on 2022-03-25 20:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_newuser_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 25, 20, 46, 19, 248598, tzinfo=utc)),
        ),
    ]
