from django.db import models
from DentistRoll.models import Clinic, Dentist
from SaloonRoll.models import Saloon, Saloon_owner
from ManagerRoll.models import Manager
from PlannerRoll.models import Planner
from TechnicianRoll.models import Technician
# Create your models here.

class Case(models.Model):
    GENDER_CHOICES = (
        ("male","male"),
        ("female","female"),
        ("other","other")
        )
    
    ORTHODONTIC_CHOICES = (
        ("yes","yes"),
        ("no","no")
        )

    TREATMENT_REQUIRED_CHOICES = (
        ("full treatment","full treatment"),
        ("continuation","continuation"),
        ("refinement","refinement"),
        ("retainer","retainer")
    )

    SECTION_CHOICES = (
        ("both arches","both arches"),
        ("upper only","upper only"),
        ("lower only","lower only")
    )

    TREATMENT_CHOICES = (
        ("essential","essential"),
        ("advance","advance"),
        ("comprehensive","comprehensive")
    )
    

    clinic                          = models.ForeignKey(Clinic, on_delete=models.DO_NOTHING,null=True,blank=True)
    dentist                         = models.ForeignKey(Dentist, on_delete=models.DO_NOTHING, null=True, blank=True)
    saloon_owner                    = models.ForeignKey(Saloon_owner, on_delete=models.DO_NOTHING, null=True, blank=True)
    saloon                          = models.ForeignKey(Saloon, on_delete=models.DO_NOTHING, null=True, blank=True)
    name                            = models.CharField(max_length=250)
    surname                         = models.CharField(max_length=250,null=True, blank=True)
    gender                          = models.CharField(max_length=50,choices=GENDER_CHOICES)
    age                             = models.IntegerField(null=True, blank=True)
    treatment_required              = models.CharField(max_length=100,choices=TREATMENT_REQUIRED_CHOICES)
    orthodontic_treatment_past      = models.CharField(max_length=10,null=True, blank=True, choices=ORTHODONTIC_CHOICES)
    section                         = models.CharField(max_length=250,null=True, blank=True, choices=SECTION_CHOICES)
    treatment_type                  = models.CharField(max_length=250,null=True, blank=True, choices=TREATMENT_CHOICES)
    upper_jaw                       = models.FileField(upload_to="upper_jaws",null=True, blank=True)
    lower_jaw                       = models.FileField(upload_to="lower_jaws",null=True, blank=True)
    rquest_collection               = models.BooleanField(default=False)
    additional_information          = models.TextField(null=True, blank=True)
    planner                         = models.ForeignKey(Planner,on_delete=models.DO_NOTHING, null=True, blank=True)
    technician                      = models.ForeignKey(Technician,on_delete=models.DO_NOTHING, null=True, blank=True)
    status                          = models.CharField(max_length=250, default="new", null=True, blank=True)
    ortho_id                        = models.CharField(max_length=255, null=True, blank=True)
    aligners_upper                  = models.IntegerField(null=True, blank=True)
    aligners_lower                  = models.IntegerField(null=True, blank=True)
    retainer_upper                  = models.IntegerField(null=True, blank=True)
    retainer_lower                  = models.IntegerField(null=True, blank=True)
    treatment_plan_upper            = models.IntegerField(null=True, blank=True)
    treatment_plan_lower            = models.IntegerField(null=True, blank=True)
    duration                        = models.IntegerField(null=True, blank=True)
    progress                        = models.CharField(max_length=255, null=True, blank=True)
    created_at                      = models.DateField(auto_now_add=True, null=True)

    fee_cleared                     = models.BooleanField(default=False)
    totel_fee                       = models.FloatField(default=0.0,null=True,blank=True)

    manager_paid                    = models.BooleanField(default=False)
    planner_paid                    = models.BooleanField(default=False)
    technician_paid                 = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Cases"

    def __str__(self):
        return str(self.name)

class Case_additional_images(models.Model):
    image                          = models.ImageField(upload_to="Additional_images")
    case                           = models.ForeignKey(Case,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Case additional images"

    def __str__(self):
        return str(self.case.name)


class Case_additional_videos(models.Model):
    video                          = models.FileField(upload_to='videos_uploaded')
    case                           = models.ForeignKey(Case,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Case additional Videos"

    def __str__(self):
        return str(self.case.name)