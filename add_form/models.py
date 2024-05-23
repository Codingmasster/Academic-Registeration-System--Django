from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    # roll_num= models.AutoField()
    user= models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    email = models.EmailField(null=True,blank=True)
    image = models.ImageField(upload_to="Pictures")
    file = models.FileField(upload_to="Files")
    final_marks = models.IntegerField(default=1)
