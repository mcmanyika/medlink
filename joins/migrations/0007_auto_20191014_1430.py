# Generated by Django 2.2.6 on 2019-10-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0006_remove_t_acct_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_acct',
            name='dob',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='t_acct',
            name='middle_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
