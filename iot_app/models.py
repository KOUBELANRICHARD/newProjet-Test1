from django.db import models

class Client(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Device(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='devices')
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200) 
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

