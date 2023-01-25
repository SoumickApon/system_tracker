from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    employees = models.ManyToManyField(User, related_name='companies')

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True)
    model = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    assigned_employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='devices')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, default='available')
    checked_out = models.BooleanField(default=False)
    condition_at_checkout = models.CharField(max_length=255, blank=True)
    condition_at_return = models.CharField(max_length=255, blank=True, default="N/A")


    def __str__(self):
        return self.name
