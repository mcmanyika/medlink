# Generated by Django 2.2.6 on 2020-01-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0028_auto_20200128_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_accts',
            name='acct_company',
            field=models.IntegerField(),
        ),
    ]