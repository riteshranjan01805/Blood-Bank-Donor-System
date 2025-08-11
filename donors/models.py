from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Donor(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    contact = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    last_donated = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class BloodRequest(models.Model):
    patient_name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3, choices=Donor.BLOOD_GROUPS)
    contact = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    reason = models.TextField()
    status = models.CharField(max_length=10, default="Pending")

    def __str__(self):
        return self.patient_name
