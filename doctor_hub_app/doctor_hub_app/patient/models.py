from django.db import models
from django.contrib.auth.hashers import make_password

class Patients(models.Model):
    Patient_Name = models.CharField(max_length=50, default="")
    Patient_Email = models.CharField(max_length=50, default="")
    Patient_Password = models.CharField(max_length=128)  # Increase length to accommodate hashed passwords
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=350)

    @property
    def get_name(self):
        return self.Patient_Name

    @property
    def get_id(self):
        return self.id
