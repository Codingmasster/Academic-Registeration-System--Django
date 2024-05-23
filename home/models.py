from django.db import models

# Create your models here.
class Student(models.Model):
    # roll_num= models.AutoField()
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    email = models.EmailField(null=True,blank=True)
    image = models.ImageField()
    file = models.FileField()
    final_marks = models.IntegerField(default=0)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price=models.FloatField()
    def __str__(self) -> str:
        return self.name
''' CRUD operations
C for Creating
R for reading
U for updating
D for deleting
'''