# Generated by Django 2.2.6 on 2020-01-28 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0027_t_accts_acct_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_accts',
            name='acct_company',
            field=models.CharField(max_length=10),
        ),
    ]
