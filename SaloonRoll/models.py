from django.db import models
from Users.models import Account as Users
from ManagerRoll.models import Manager
# Create your models here.

class Saloon(models.Model):
    name                    = models.CharField(max_length=150, unique=True)
    building_number         = models.CharField(max_length=50)
    street                  = models.CharField(max_length=150)
    town                    = models.CharField(max_length=150)
    postcode                = models.CharField(max_length=150)
    country                 = models.CharField(max_length=150)
    number                  = models.CharField(max_length=50)
    email                   = models.EmailField()

    class Meta:
        verbose_name_plural = "Saloons"

    def __str__(self):
        return self.name

class Saloon_owner(models.Model):
    user                    = models.OneToOneField(Users, on_delete=models.CASCADE)
    surname                 = models.CharField(max_length=150,null=True,blank=True)
    number                  = models.CharField(max_length=150,null=True,blank=True)
    saloon                  = models.ManyToManyField(Saloon)
    manager                 = models.ForeignKey(Manager, on_delete=models.DO_NOTHING, null=True, blank=True)
    code                    = models.CharField(max_length=150,null=True,blank=True)

    class Meta:
        verbose_name_plural = "Saloon Owners"

    def __str__(self):
        return self.user.username






