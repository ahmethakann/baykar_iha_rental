# Generated by Django 4.1.7 on 2023-03-14 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_ihadealer_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iha',
            name='capacity',
        ),
    ]