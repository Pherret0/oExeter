# Generated by Django 3.1.6 on 2021-02-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('owner', models.CharField(max_length=45)),
                ('set_date_time', models.DateField()),
                ('end_date_time', models.DateField()),
                ('location', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=500)),
                ('min_attendees', models.IntegerField()),
                ('max_attendees', models.IntegerField()),
            ],
        ),
    ]
