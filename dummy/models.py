from django.db import models

# Create your models here.
class Contact(models.Model):
    usn=models.CharField(max_length=50,primary_key="True")
    name=models.CharField(max_length=50,default="")
    sem=models.CharField(max_length=50,default="")
    num=models.CharField(max_length=50,default="")
    mail=models.CharField(max_length=50,default="")


    def __str__(self):
        return self.name
