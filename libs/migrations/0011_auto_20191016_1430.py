# Generated by Django 2.2.6 on 2019-10-16 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0010_auto_20191011_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Daily_Login_ID',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Daily_Logout_ID',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]