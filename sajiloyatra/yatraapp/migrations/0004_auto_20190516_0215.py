from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yatraapp', '0003_auto_20190516_0052'),
    ]

    operations = [

        migrations.AddField(
            model_name='festival',
            name='festival_image',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='checkin',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='food',
            name='checkout',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='food',
            name='food_image_url',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='month',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='ethinic',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='festival_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='festival',
            name='month',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

