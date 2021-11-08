# Generated by Django 3.2.9 on 2021-11-04 09:49

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('user_name', models.CharField(max_length=100)),
                ('user_DOB', models.DateField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100)),
                ('task_type', models.CharField(max_length=100)),
                ('task_description', models.CharField(max_length=200)),
                ('task_start_time', models.DateTimeField(verbose_name=datetime.datetime(2021, 11, 4, 9, 49, 48, 794557))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.person')),
            ],
        ),
        migrations.DeleteModel(
            name='Temp',
        ),
    ]
