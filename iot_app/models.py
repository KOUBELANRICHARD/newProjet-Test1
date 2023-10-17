from django.db import models

class Client(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, verbose_name="Actif")
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.full_name

class Device(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='devices')
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200) 
    image = models.ImageField(upload_to='devices/')
    last_updated = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True, verbose_name="Est actif")
    
    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"

    def __str__(self):
        return self.name

