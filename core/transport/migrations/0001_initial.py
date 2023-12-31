# Generated by Django 5.0 on 2023-12-31 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_place', models.CharField(max_length=50)),
                ('end_place', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('default_temperature', models.FloatField()),
                ('default_humidity', models.FloatField()),
                ('delta_temperature', models.FloatField()),
                ('delta_humidity', models.FloatField()),
                ('air_conditioner_temperature', models.FloatField()),
                ('nebulizer_status', models.FloatField()),
            ],
        ),
    ]
