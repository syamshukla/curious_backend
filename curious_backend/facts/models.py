from django.db import models

# Create your models here.
class Facts(models.Model):
   id= models.AutoField(primary_key=True)
   body = models.CharField(max_length=30)
   category = models.CharField(max_length=30)

   def __str__(self):
      return self.body
   
class Categories(models.Model):
   id= models.AutoField(primary_key=True)
   name= models.CharField(max_length=30)

   def __str__(self):
      return self.body