from django.db import models
from Users.models import Account as Users
# Create your models here.

class Technician(models.Model):
    user                    = models.OneToOneField(Users, on_delete=models.CASCADE)
    number                  = models.CharField(max_length=150,null=True,blank=True)
    fee                     = models.FloatField(null=True,blank=True)
    outstanding             = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Technicians"

    def __str__(self):
        return self.user.username