from django.db import models

# Create your models here.
class employee(models.Model):
    first_name=models.CharField(max_length=100);
    last_name=models.CharField(max_length=100);
    photo=models.ImageField(upload_to='images');
    designation=models.CharField(max_length=100);
    email_address=models.EmailField(max_length=100);
    phone_number=models.CharField(max_length=10);
    