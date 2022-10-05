from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    mobile_number = models.CharField(null=True,max_length=15)
    username = models.CharField(unique=True,max_length=100,null=True, blank=True)
    permanent_address = models.CharField(max_length=100,null=True)
    residential_address = models.CharField(max_length=100,null=True)
    lga = models.CharField(max_length=20, null=True, blank=True)
    nin_number = models.PositiveBigIntegerField(null=True)
    avatar = models.ImageField(null=True)
    date_registered = models.DateField(default=now,editable=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class Areas(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(decimal_places=8,max_digits=12)
    longitude = models.DecimalField(decimal_places=8,max_digits=12)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Room(models.Model):
    name = models.CharField(max_length=50)
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True)
    available = models.BooleanField(default=True)
    address = models.CharField(max_length=100, null=True)
    latitude = models.FloatField(max_length=12)
    longitude = models.FloatField(max_length=12)
    description = models.TextField()
    first_image = models.ImageField(null=True)
    second_image = models.ImageField(null=True)
    third_image = models.ImageField(null=True)
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Items(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    contact_number = models.CharField(null=True,max_length=15)
    
    TYPE_CHOICES = [
        ('LEASE', 'Lease'),
        ('SELL', 'Sell')
    ]
    
    type = models.CharField(max_length=20,choices=TYPE_CHOICES,default='SELL')
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    first_image = models.ImageField(null=True)
    second_image = models.ImageField(null=True)
    third_image = models.ImageField(null=True)
    
    def __str__(self):
        return self.product_name