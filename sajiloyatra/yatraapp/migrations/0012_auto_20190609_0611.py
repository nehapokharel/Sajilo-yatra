# Generated by Django 2.2.1 on 2019-06-09 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yatraapp', '0011_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventcompletion',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]