# Generated by Django 4.2.7 on 2023-11-06 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('standard', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='danielAgency.city')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateField()),
                ('return_date', models.DateField()),
                ('number_of_days', models.PositiveIntegerField()),
                ('trip_type', models.CharField(choices=[('BB', 'Bed & Breakfast'), ('HB', 'Half Board'), ('FB', 'Full Board'), ('AI', 'All Inclusive')], max_length=2)),
                ('price_adult', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_child', models.DecimalField(decimal_places=2, max_digits=10)),
                ('promoted', models.BooleanField()),
                ('num_places_adult', models.PositiveIntegerField()),
                ('num_places_child', models.PositiveIntegerField()),
                ('from_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='danielAgency.airport')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='danielAgency.city')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='danielAgency.city')),
                ('to_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='danielAgency.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_details', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='danielAgency.trip')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='danielAgency.continent')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='danielAgency.country'),
        ),
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='danielAgency.city'),
        ),
    ]