# Generated by Django 2.2.6 on 2019-11-06 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0019_t_batch_billing_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_batch',
            name='payment_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
