# Generated by Django 2.2.6 on 2019-11-04 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0022_auto_20191104_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_oig',
            name='root',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]