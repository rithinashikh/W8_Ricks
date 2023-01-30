from django.db import models

from django.db import models

class UserDetails(models.Model):
    username=models.CharField(unique=True, max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    active=models.BooleanField(default=True)
    def __str__(self): 
        return self.username 

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name    

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='imagestore/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
