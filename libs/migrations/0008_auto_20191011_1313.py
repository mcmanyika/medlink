# Generated by Django 2.2.6 on 2019-10-11 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0007_auto_20190712_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Daily_Login_ID', models.CharField(default='', max_length=20)),
                ('Daily_Logout_ID', models.CharField(default='', max_length=20)),
                ('user', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='t_patient_acct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=10, null=True)),
                ('lname', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('user', models.IntegerField(blank=True, default=1, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Daily',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
        migrations.AddField(
            model_name='client',
            name='PatientID',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='libs.t_patient_acct'),
        ),
    ]
