# Generated by Django 2.2.3 on 2019-07-06 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0005_daily_root_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daily',
            name='root_id',
        ),
    ]