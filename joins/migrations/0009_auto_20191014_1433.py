# Generated by Django 2.2.6 on 2019-10-14 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0008_auto_20191014_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_acct',
            name='doh',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
