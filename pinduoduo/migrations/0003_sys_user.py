# Generated by Django 2.0.1 on 2020-05-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinduoduo', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sys_user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]
