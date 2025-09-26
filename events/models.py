from django.db import models
from django.contrib.auth.models import User


# ----------------------------
# Service Category Model
# ----------------------------
class ServiceCategory(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


# ----------------------------
# Service Model
# ----------------------------
class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, related_name='services', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True) # placeholder path or URL

    def __str__(self):
        return self.title


# ----------------------------
# Package Model
# ----------------------------
class Package(models.Model):
    service = models.ForeignKey(Service, related_name='packages', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


# ----------------------------
# Portfolio Item Model
# ----------------------------
class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


# ----------------------------
# Booking Model
# ----------------------------
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField()
    time = models.TimeField()
    requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking {self.user} - {self.service} on {self.date}'
