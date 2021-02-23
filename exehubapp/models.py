# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attendees(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    event = models.ForeignKey('Events', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'attendees'
        unique_together = (('user', 'event'),)


class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=50)
    event_owner = models.CharField(max_length=747, blank=True, null=True)
    group = models.ForeignKey('UniGroups', models.DO_NOTHING)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    attendees_min = models.PositiveSmallIntegerField(blank=True, null=True)
    attendees_max = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class Members(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    group = models.ForeignKey('UniGroups', models.DO_NOTHING)
    is_group_admin = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'members'
        unique_together = (('user', 'group'),)


class UniGroups(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(unique=True, max_length=50)
    group_owner = models.CharField(max_length=747, blank=True, null=True)
    group_email = models.CharField(unique=True, max_length=254)
    group_irc = models.CharField(unique=True, max_length=200, blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'uni_groups'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    is_server_admin = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    email = models.CharField(unique=True, max_length=254)
    irc_username = models.CharField(max_length=9, blank=True, null=True)
    password_hash = models.CharField(max_length=64)
    name = models.CharField(max_length=747)

    class Meta:
        managed = False
        db_table = 'users'
