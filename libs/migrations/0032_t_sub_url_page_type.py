# Generated by Django 2.2.6 on 2019-11-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0031_t_sub_url_toggle'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_sub_url',
            name='page_type',
            field=models.CharField(default='', max_length=20),
        ),
    ]
