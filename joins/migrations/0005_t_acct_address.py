# Generated by Django 2.2.6 on 2019-10-11 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0004_auto_20191011_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_acct',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
