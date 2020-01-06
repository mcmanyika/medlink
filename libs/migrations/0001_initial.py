# Generated by Django 2.2.3 on 2019-07-06 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('veh_reg', models.CharField(default='', max_length=10)),
                ('driver', models.CharField(blank=True, max_length=10, null=True)),
                ('amount', models.IntegerField()),
                ('notes', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.IntegerField(blank=True, default=1, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]