# Generated by Django 2.2.6 on 2019-10-14 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20191014_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='t_care_giver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('care_attendant', models.IntegerField(blank=True, default=1, null=True)),
                ('user', models.IntegerField(blank=True, default=1, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tracker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.t_client')),
            ],
        ),
    ]
