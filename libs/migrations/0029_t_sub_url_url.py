# Generated by Django 2.2.6 on 2019-11-19 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0028_t_url_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_sub_url',
            name='url',
            field=models.CharField(default='', max_length=100),
        ),
    ]
