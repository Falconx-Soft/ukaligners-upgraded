from django.contrib import admin
from .models import Case, Case_additional_images, Case_additional_videos
# Register your models here.

class Case_admin(admin.ModelAdmin):
	list_display = ['name','clinic','dentist','treatment_required','orthodontic_treatment_past','section','treatment_type','rquest_collection']
	class Meta:
		model = Case

admin.site.register(Case,Case_admin)

admin.site.register(Case_additional_images)

admin.site.register(Case_additional_videos)
