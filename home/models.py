from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    short_bio = models.CharField(max_length=200)
    profile = models.ImageField(upload_to='images/', default='empty.jpg') 

    def __str__(self):
        return self.name

