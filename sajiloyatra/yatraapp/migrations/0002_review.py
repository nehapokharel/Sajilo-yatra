# Generated by Django 2.2.1 on 2019-06-23 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yatraapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer', models.CharField(max_length=500)),
                ('review', models.TextField()),
                ('festival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yatraapp.Festival')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yatraapp.Food')),
            ],
        ),
    ]
