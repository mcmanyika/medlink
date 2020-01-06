# Generated by Django 2.2.3 on 2019-07-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily',
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
        migrations.RenameField(
            model_name='vehicle',
            old_name='veh_reg',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='date',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='img',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='notes',
        ),
    ]
