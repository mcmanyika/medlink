# Generated by Django 2.2.3 on 2019-07-06 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0003_auto_20190706_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='veh_reg',
            field=models.CharField(default='', max_length=20),
        ),
    ]
