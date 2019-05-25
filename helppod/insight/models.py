from django.db import models
from django import forms


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    service_date=models.DateField()
    service_time=models.TimeField()
    pickup_location=models.CharField(max_length=100)
    drop_location=models.CharField(max_length=100)  
    phone=models.CharField(max_length=10)
    user_name = models.CharField( max_length =100, default=None)      
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False )

    def __str__(self): #unicode
        return self.title
    
    class Meta:
        ordering = ["-timestamp"]

class HelperSignUp(models.Model):
    first_name=models.CharField(max_length=100) 
    last_name=models.CharField(max_length=100)#max length is required field
    email = models.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    # confirm_Password =forms.CharField(widget=forms.PasswordInput)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self): #unicode
        return self.email

    
