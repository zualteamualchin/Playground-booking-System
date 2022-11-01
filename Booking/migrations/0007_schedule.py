# Generated by Django 4.0.6 on 2022-07-23 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0006_location_local'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(blank=True)),
                ('AM5', models.BooleanField(default=False)),
                ('AM6', models.BooleanField(default=False)),
                ('AM7', models.BooleanField(default=False)),
                ('AM8', models.BooleanField(default=False)),
                ('AM9', models.BooleanField(default=False)),
                ('AM10', models.BooleanField(default=False)),
                ('AM11', models.BooleanField(default=False)),
                ('AM12', models.BooleanField(default=False)),
                ('PM1', models.BooleanField(default=False)),
                ('PM2', models.BooleanField(default=False)),
                ('PM3', models.BooleanField(default=False)),
                ('PM4', models.BooleanField(default=False)),
                ('PM5', models.BooleanField(default=False)),
                ('PM6', models.BooleanField(default=False)),
                ('PM7', models.BooleanField(default=False)),
                ('PM8', models.BooleanField(default=False)),
                ('PM9', models.BooleanField(default=False)),
                ('PM10', models.BooleanField(default=False)),
            ],
        ),
    ]
