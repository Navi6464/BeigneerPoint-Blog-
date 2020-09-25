from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
      contact_id = models.AutoField(primary_key=True)
      name = models.CharField(max_length=100)
      email = models.CharField(max_length=120)
      mesg = models.TextField()

      def __str__(self):
          return self.name



class Topic(models.Model):
      topic_id = models.AutoField(primary_key=True)
      topic_name = models.CharField(max_length=80)
      desc = models.TextField()
      name = models.TextField()
      image = models.ImageField(upload_to='image')
      date = models.DateField()
      
      def __str__(self):
          return self.topic_name
      
class News(models.Model):
      news_id = models.AutoField(primary_key=True)
      email = models.CharField(max_length=120)
      
      def __str__(self):
          return "News request by" + self.email

class BlogComment(models.Model):
      sno = models.AutoField(primary_key=True)
      comment = models.TextField()
      user = models.CharField(max_length=49)
      post_name= models.CharField(max_length=90)
      timestamp = models.DateTimeField(default=now)  

      def __str__(self):
          return "comment by "+ self.user + " in post "+self.post_name 
      



      
   

       
