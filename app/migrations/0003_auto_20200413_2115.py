# Generated by Django 2.0.3 on 2020-04-13 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200411_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobmodel',
            name='pub_time',
        ),
        migrations.RemoveField(
            model_name='jobmodel',
            name='welfare',
        ),
    ]