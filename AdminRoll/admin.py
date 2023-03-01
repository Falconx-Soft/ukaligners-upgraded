from django.contrib import admin
from .models import fee
# Register your models here.


class Case_fee(admin.ModelAdmin):
	list_display = ['fee_plan','fee_retainer','fee_aligner','fee_monitring','fee_comprehensive']
	class Meta:
		model = fee

admin.site.register(fee,Case_fee)