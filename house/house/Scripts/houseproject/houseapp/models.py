from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='category' 

    def __str__(self):
        return self.category_name

class Property(models.Model):
    img=models.FileField(upload_to='videos/',default='')
    owner_name=models.CharField(max_length=30)
    price=models.CharField(max_length=40)
    bhk=models.CharField(max_length=30)
    contact=models.CharField(max_length=15)
    city=models.CharField(max_length=30,default='unknown')
    address=models.TextField(max_length=300)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='property'

    def __str__(self):
        return self.category.category_name


class Shortlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Property,on_delete=models.CASCADE)

    class Meta:
        db_table='shortlist'
    
    def __str__(self):
        return self.product.owner_name






