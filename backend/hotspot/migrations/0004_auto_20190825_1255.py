# Generated by Django 2.1.4 on 2019-08-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotspot', '0003_remove_hotspot_last_fetch_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotspotsource',
            name='desc',
            field=models.CharField(blank=True, help_text='描述', max_length=128),
        ),
    ]