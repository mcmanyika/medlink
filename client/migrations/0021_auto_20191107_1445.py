# Generated by Django 2.2.6 on 2019-11-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0020_t_batch_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_batch',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
