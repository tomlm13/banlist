# Generated by Django 2.0.7 on 2020-06-18 19:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('banuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneduser',
            name='ban_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 6, 18, 19, 16, 32, 84650, tzinfo=utc)),
        ),
    ]
