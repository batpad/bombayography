# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Area(models.Model):
    areaid = models.IntegerField(primary_key=True)
    area_code = models.BigIntegerField()
    area_name = models.CharField(max_length=256)
    class Meta:
        db_table = u'area'

class Atlas(models.Model):
    atlasid = models.IntegerField(primary_key=True)
    route = models.CharField(max_length=128)
    routcode = models.CharField(max_length=128)
    src = models.CharField(max_length=256)
    first_src = models.FloatField()
    last_src = models.FloatField()
    dest = models.CharField(max_length=256)
    first_dest = models.FloatField()
    last_dest = models.FloatField()
    routdist = models.FloatField()
    run_time1 = models.CharField(max_length=128)
    run_time2 = models.CharField(max_length=128)
    run_time3 = models.CharField(max_length=128)
    run_time4 = models.CharField(max_length=128)
    frequency1 = models.CharField(max_length=128)
    frequency2 = models.CharField(max_length=128)
    frequency3 = models.CharField(max_length=128)
    frequency4 = models.CharField(max_length=128)
    schedule = models.CharField(max_length=128)
    class Meta:
        db_table = u'atlas'

class Route(models.Model):
    routeid = models.IntegerField(primary_key=True)
    routcode = models.CharField(max_length=128)
    stop_sr = models.BigIntegerField()
    stop_code = models.BigIntegerField()
    stage_code = models.CharField(max_length=128)
    kms = models.FloatField()
    area_code = models.BigIntegerField()
    class Meta:
        db_table = u'route'

class Stop(models.Model):
    stopid = models.IntegerField(primary_key=True)
    stopcode = models.BigIntegerField()
    stopname = models.CharField(max_length=128)
    areacode = models.BigIntegerField()
    areaname = models.CharField(max_length=128)
    class Meta:
        db_table = u'stop'

