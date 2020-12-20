# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# Create your models here.


class Movies(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)




