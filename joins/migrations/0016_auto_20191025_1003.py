# Generated by Django 2.2.6 on 2019-10-25 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0015_auto_20191023_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_client_attribute',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='t_client_attribute',
            name='updated',
        ),
    ]
