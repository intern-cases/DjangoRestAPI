# Generated by Django 2.2.4 on 2019-08-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dealer', '0003_auto_20190820_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
