# Generated by Django 2.2.6 on 2019-10-16 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0011_auto_20191016_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='PatientID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]