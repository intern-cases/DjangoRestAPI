# Generated by Django 2.2.4 on 2019-08-19 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, serialize=False, unique=True)),
                ('working_area', models.CharField(max_length=30)),
                ('establish_year', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(default='POINT(0.0 0.0)', srid=4326)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
