# Generated by Django 2.0.7 on 2020-06-18 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banuser', '0002_auto_20200618_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneduser',
            name='ban_date',
            field=models.DateTimeField(verbose_name='Date Banned'),
        ),
    ]
