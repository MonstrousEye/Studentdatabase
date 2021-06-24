from django.db import models

# Create your models here.
class Form(models.Model):
    sno=models.IntegerField(primary_key=True)
    fname=models.CharField(max_length=50,default="")
    lname=models.CharField(max_length=10,default="")
    branch=models.CharField(max_length=25,default="")
    sem=models.IntegerField(default="")
    phone=models.CharField(max_length=12,default="")
    email=models.CharField(max_length=70,default="")
    college=models.CharField(max_length=70,default="")
    city=models.CharField(max_length=50,default="")
    state=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.fname