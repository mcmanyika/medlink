# Generated by Django 2.2.6 on 2019-10-30 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0016_auto_20191025_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_employee_attribute',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='t_employee_attribute',
            name='updated',
        ),
    ]
