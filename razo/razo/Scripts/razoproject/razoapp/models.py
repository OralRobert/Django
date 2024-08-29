from django.db import models

# Create your models here.

class Coffee(models.Model):
    name=models.CharField(max_length=30)
    amount=models.CharField(max_length=30)
    payment_id=models.CharField(max_length=100)
    paid=models.BooleanField(default=False)
    
    class Meta:
        db_table='coffee'
