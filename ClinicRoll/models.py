# Create your models here.
from django.db import models
from Users.models import Account as Users
# Create your models here.

class Clinic(models.Model):
    user                    = models.OneToOneField(Users, on_delete=models.CASCADE)
    building_number         = models.CharField(max_length=150)
    street                  = models.CharField(max_length=150)
    town                    = models.CharField(max_length=150)
    postcode                = models.CharField(max_length=150)
    country                 = models.CharField(max_length=150)
    number                  = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Clinics"

    def __str__(self):
        return self.user.username