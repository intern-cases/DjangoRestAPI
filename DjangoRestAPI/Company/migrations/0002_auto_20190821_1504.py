# Generated by Django 2.2.4 on 2019-08-21 15:04

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default='POINT(41.06 28.99)', srid=4326),
        ),
    ]
