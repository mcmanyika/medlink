# Generated by Django 2.2.6 on 2019-10-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_auto_20191028_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_billing_tracker',
            name='previous_denial_reason',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
