# Generated by Django 2.2.6 on 2019-10-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_auto_20191029_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='t_bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_number', models.IntegerField(blank=True, null=True)),
                ('billing_date', models.DateField()),
                ('user', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='t_billing',
        ),
    ]
