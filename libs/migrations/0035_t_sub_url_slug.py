# Generated by Django 2.2.6 on 2019-11-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0034_auto_20191127_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_sub_url',
            name='slug',
            field=models.SlugField(default='', max_length=100, unique=True),
        ),
    ]