from django.db import models
from Users.models import Account as Users
from ManagerRoll.models import Manager
from ClinicRoll.models import Clinic
# Create your models here.

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
