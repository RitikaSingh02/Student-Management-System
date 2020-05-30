from django.db import models
class users(models.Model):
    USER_NAME=models.CharField(max_length=250)
    PASSWORD=models.CharField(max_length=250,default="KIET123")
    USERTYPE=models.CharField(max_length=250)
    

    def __str__(self):#what this function is doing is that when Album.objects.all() then the objects of the class are printed like the below returned in the function
        return self.USER_NAME + '-' + self.USERTYPE
class students(models.Model):
    
    USER_NAME=models.CharField(max_length=250,default="NULL")
    PASSWORD=models.CharField(max_length=250,default="KIET123")
    father_name=models.CharField(max_length=250)
    email=models.CharField(max_length=250,unique=True)
    branch=models.CharField(max_length=250)
    phone_no=models.BigIntegerField(unique=True)
# Create your models here.
