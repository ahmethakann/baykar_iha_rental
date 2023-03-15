# Generated by Django 4.1.7 on 2023-03-15 10:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Iha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('is_available', models.BooleanField(default=True)),
                ('rent', models.CharField(blank=True, max_length=50)),
                ('operational_altitude', models.CharField(blank=True, max_length=50, null=True)),
                ('max_altitude', models.CharField(blank=True, max_length=50, null=True)),
                ('max_flight_time', models.CharField(blank=True, max_length=50, null=True)),
                ('payload_capacity', models.CharField(blank=True, max_length=50, null=True)),
                ('communication_range', models.CharField(blank=True, max_length=50, null=True)),
                ('fuel_capacity', models.CharField(blank=True, max_length=50, null=True)),
                ('cruise_speed', models.CharField(blank=True, max_length=50, null=True)),
                ('max_speed', models.CharField(blank=True, max_length=50, null=True)),
                ('max_takeoff_weight', models.CharField(blank=True, max_length=50, null=True)),
                ('height', models.CharField(blank=True, max_length=50, null=True)),
                ('wingspan', models.CharField(blank=True, max_length=50, null=True)),
                ('length', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IhaDealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(50)])),
                ('earnings', models.IntegerField(default=0)),
                ('type', models.CharField(blank=True, max_length=20)),
                ('iha_dealer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.CharField(max_length=50)),
                ('days', models.IntegerField(default=1)),
                ('is_complete', models.BooleanField(default=False)),
                ('iha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.iha')),
                ('iha_dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ihadealer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ihadealer',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.location'),
        ),
        migrations.AddField(
            model_name='iha',
            name='iha_dealer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.ihadealer'),
        ),
        migrations.AddField(
            model_name='iha',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.location'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('type', models.CharField(blank=True, max_length=50)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
