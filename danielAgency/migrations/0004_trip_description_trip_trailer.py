# Generated by Django 4.2.7 on 2023-11-23 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danielAgency', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='trailer',
            field=models.URLField(blank=True),
        ),
    ]
