# Generated by Django 4.0.6 on 2022-07-23 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0009_alter_scheduler_day'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Scheduler',
        ),
    ]
