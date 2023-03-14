# Generated by Django 4.1.7 on 2023-03-14 06:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customer_iha_ihadealer_location_order_delete_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='iha',
            name='communication_range',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iha',
            name='cruise_speed',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iha',
            name='fuel_capacity',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iha',
            name='height',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iha',
            name='lenght',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iha',
            name='max_altitude',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iha',
            name='max_flight_time',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iha',
            name='max_speed',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iha',
            name='max_takeoff_weight',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iha',
            name='operational_altitude',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iha',
            name='payload_capacity',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='iha',
            name='rent',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='iha',
            name='wingspan',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ihadealer',
            name='phone',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(50), django.core.validators.MaxLengthValidator(50)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='days',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='rent',
            field=models.CharField(max_length=50),
        ),
    ]
