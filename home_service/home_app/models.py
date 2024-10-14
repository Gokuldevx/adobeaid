from django.db import models

# Create your models here.

class sermodel(models.Model):
    spid=models.CharField(max_length=12)
    sname=models.CharField(max_length=100)
    desc=models.CharField(max_length=200)
    simg=models.FileField(upload_to='images')

    class Meta:
        db_table="services"

