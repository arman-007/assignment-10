# Generated by Django 5.1.4 on 2025-01-02 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('property_title', models.TextField()),
                ('rating', models.FloatField(blank=True, null=True)),
                ('location', models.TextField()),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('room_type', models.TextField()),
                ('price', models.FloatField()),
                ('city_name', models.TextField()),
            ],
            options={
                'db_table': 'hotels',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GeneratedTitle',
            fields=[
                ('hotel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='property_app.hotel')),
                ('generated_title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HotelRating',
            fields=[
                ('hotel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='property_app.hotel')),
                ('rating', models.TextField()),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HotelSummary',
            fields=[
                ('hotel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='property_app.hotel')),
                ('summary', models.TextField()),
            ],
        ),
    ]
