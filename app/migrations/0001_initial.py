# Generated by Django 3.0.5 on 2020-05-24 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(default='', max_length=10)),
                ('branch', models.CharField(default='', max_length=25)),
                ('sem', models.IntegerField(default='')),
                ('phone', models.CharField(default='', max_length=12)),
                ('email', models.CharField(default='', max_length=70)),
                ('college', models.CharField(default='', max_length=70)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
