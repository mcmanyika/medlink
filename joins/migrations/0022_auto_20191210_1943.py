# Generated by Django 2.2.6 on 2019-12-10 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0021_delete_t_acct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_client_attribute',
            name='soc',
            field=models.DateField(blank=True, null=True),
        ),
    ]
