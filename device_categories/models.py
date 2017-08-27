from django.db import models

# Create your models here.
class Type(models.Model):
    device_category = models.CharField(max_length=20)   # Just focusing on categories for right now

    def __str__(self):
        return self.device_category

class Device(models.Model):
    category = models.ForeignKey(Type, on_delete=models.CASCADE)
    tms_code = models.CharField(max_length=5)
    device_name = models.CharField(max_length=30)
    device_count = models.CharField(max_length=3)

    def __str__(self):
        return "Device: " + self.device_name