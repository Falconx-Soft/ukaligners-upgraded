from django.db import models

# Create your models here.

class fee(models.Model):
    fee_plan                       = models.IntegerField(default=0.0)
    fee_retainer                   = models.IntegerField(default=0.0)
    fee_aligner                    = models.IntegerField(default=0.0)
    fee_monitring                  = models.IntegerField(default=0.0)
    fee_comprehensive              = models.IntegerField(default=0.0)

    class Meta:
        verbose_name_plural = "Fee"

    def __str__(self):
        return "Fee"
