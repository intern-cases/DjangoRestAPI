# Generated by Django 2.2.4 on 2019-08-19 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('declaration', models.CharField(max_length=500)),
                ('photo', models.ImageField(null=True, upload_to='db')),
                ('price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('location', django.contrib.gis.db.models.fields.PointField(default='POINT(0.0 0.0)', srid=4326)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
