# Generated by Django 2.2.6 on 2019-10-23 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0013_auto_20191023_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_accts',
            name='ssn',
        ),
        migrations.RemoveField(
            model_name='t_accts',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='t_accts',
            name='updated',
        ),
    ]