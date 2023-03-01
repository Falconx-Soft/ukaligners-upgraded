from django.contrib import admin
from .models import *
# Register your models here.

class Saloon_owner_admin(admin.ModelAdmin):
	list_display = ['user','surname','number','manager','code']
	class Meta:
		model = Saloon_owner

admin.site.register(Saloon_owner,Saloon_owner_admin)


class Saloon_admin(admin.ModelAdmin):
	list_display = ['name','building_number','street','town','postcode','country','number','email']
	class Meta:
		model = Saloon

admin.site.register(Saloon,Saloon_admin)