# Generated by Django 2.2.6 on 2019-11-06 21:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0018_t_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_batch',
            name='billing_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]