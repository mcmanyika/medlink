# Generated by Django 2.2.6 on 2019-10-23 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0014_auto_20191023_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='t_client_attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_number', models.CharField(blank=True, max_length=15, null=True)),
                ('soc', models.CharField(blank=True, max_length=15, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.IntegerField(blank=True, default=1, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rootid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joins.t_accts')),
            ],
        ),
        migrations.CreateModel(
            name='t_employee_attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(blank=True, max_length=15, null=True)),
                ('doh', models.CharField(blank=True, max_length=15, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.IntegerField(blank=True, default=1, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rootid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joins.t_accts')),
            ],
        ),
        migrations.DeleteModel(
            name='t_acct_attribute',
        ),
    ]