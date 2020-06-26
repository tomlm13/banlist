# Generated by Django 2.0.7 on 2020-06-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banned_username', models.CharField(max_length=50)),
                ('ban_date', models.DateTimeField(verbose_name='date banned')),
                ('ban_reason', models.CharField(max_length=200)),
            ],
        ),
    ]