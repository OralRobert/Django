from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class addincome(models.Model):
    income=models.IntegerField()
    income_type=models.CharField(max_length=30)
    income_date=models.DateField()
    description=models.TextField(max_length=300)
    User=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='income'

from django import forms
class addincomeform(forms.ModelForm):
    class Meta:
        model=addincome
        fields='__all__'
