from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account



class AccountAdmin(UserAdmin):
	list_display = ('username','email', 'is_superuser','is_admin','is_manager','is_planner','is_technician','is_dentist','is_salon')
	search_fields = ('email','username')
	readonly_fields=('id', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)