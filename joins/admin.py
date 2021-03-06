from django.contrib import admin

from .models import *


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'email', 'city']
	class Meta:
		model = CompanyProfile
admin.site.register(CompanyProfile, CompanyAdmin)

class AccountCompanyAdmin(admin.ModelAdmin):
	list_display = ['id', 'rootid', 'user', 'timestamp']
	class Meta:
		model = AccountCompany
admin.site.register(AccountCompany, AccountCompanyAdmin)

class UserPicAdmin(admin.ModelAdmin):
	list_display = ['id',]
	class Meta:
		model = UserProfile
admin.site.register(UserProfile, UserPicAdmin)

class AcctsAdmin(admin.ModelAdmin):
	list_display = ['id', 'fname', 'lname', 'gender', 'account_type']
	class Meta:
		model = t_accts
admin.site.register(t_accts, AcctsAdmin)


class EmployeeAttributeAdmin(admin.ModelAdmin):
	list_display = ['rootid', 'employee_id', 'doh', 'status']
	class Meta:
		model = t_employee_attribute
admin.site.register(t_employee_attribute, EmployeeAttributeAdmin)

class ClientAttributeAdmin(admin.ModelAdmin):
	list_display = ['rootid', 'client_number', 'company', 'soc', 'status']
	class Meta:
		model = t_client_attribute
admin.site.register(t_client_attribute, ClientAttributeAdmin)


class EvaluationAttributeAdmin(admin.ModelAdmin):
	list_display = ['rootid', 'employee_id', 'scheduled_date', 'status']
	class Meta:
		model = t_evaluation
admin.site.register(t_evaluation, EvaluationAttributeAdmin)