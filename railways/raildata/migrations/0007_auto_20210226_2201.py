# Generated by Django 3.1.5 on 2021-02-26 16:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('raildata', '0006_auto_20210226_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='arrivaltime',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='train',
            name='departuretime',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]