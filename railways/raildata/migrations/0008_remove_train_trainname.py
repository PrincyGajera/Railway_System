# Generated by Django 3.1.5 on 2021-02-26 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raildata', '0007_auto_20210226_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='Trainname',
        ),
    ]