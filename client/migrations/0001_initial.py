# Generated by Django 2.2.6 on 2019-10-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t_client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=20, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=12, null=True)),
                ('lname', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('ssn', models.CharField(blank=True, max_length=25, null=True)),
                ('client_number', models.IntegerField(blank=True, null=True)),
                ('soc', models.DateField(blank=True, null=True)),
                ('emergency_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.IntegerField(blank=True, default=1, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
