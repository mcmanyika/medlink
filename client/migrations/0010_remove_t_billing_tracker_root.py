# Generated by Django 2.2.6 on 2019-10-25 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_auto_20191025_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_billing_tracker',
            name='root',
        ),
    ]
