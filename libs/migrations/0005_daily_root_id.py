# Generated by Django 2.2.3 on 2019-07-06 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0004_auto_20190706_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily',
            name='root_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
