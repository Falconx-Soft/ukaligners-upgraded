from django.db import models
from Users.models import Account as Users
from ManagerRoll.models import Manager
# Create your models here.

class Clinic(models.Model):
    name                    = models.CharField(max_length=150, unique=True)
    building_number         = models.CharField(max_length=50)
    street                  = models.CharField(max_length=150)
    town                    = models.CharField(max_length=150)
    postcode                = models.CharField(max_length=150)
    country                 = models.CharField(max_length=150)
    number                  = models.CharField(max_length=50)
    email                   = models.EmailField()

    class Meta:
        verbose_name_plural = "Clinics"

    def __str__(self):
        return self.name

class Dentist(models.Model):
    user                    = models.OneToOneField(Users, on_delete=models.CASCADE)
    surname                 = models.CharField(max_length=150,null=True,blank=True)
    number                  = models.CharField(max_length=150,null=True,blank=True)
    clinic                  = models.ManyToManyField(Clinic,null=True,blank=True)
    manager                 = models.ForeignKey(Manager, on_delete=models.DO_NOTHING, null=True, blank=True)
    code                    = models.CharField(max_length=150,null=True,blank=True)

    class Meta:
        verbose_name_plural = "Dentists"

    def __str__(self):
        return self.user.username






