from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

User=get_user_model()

class customuseradmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		(_('Personal info'), {'fields': ('first_name', 'last_name')}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)

	employee_fieldsets = (
		(None, {'fields': ('email', 'password')}),
		(_('Personal info'), {'fields': ('first_name', 'last_name')}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)

	manager_fieldsets = (
		(None, {'fields': ('email', 'password')}),
		(_('Personal info'), {'fields': ('first_name', 'last_name')}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'groups',)}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2'),
		}),
	)

	list_display = ('email', 'is_staff',)
	search_fields = ('email',)
	ordering = ('date_joined',)
	list_filter = ('is_staff',)
	staff_readonly_fields = ('last_login', 'date_joined',)

	def get_readonly_fields(self, request, obj=None):
		if not request.user.is_superuser:
			return self.staff_readonly_fields
		else:
			return super(customuseradmin, self).get_readonly_fields(request, obj)

	def get_fieldsets(self, request, obj=None):
		if not request.user.is_superuser:
			if request.user.groups.filter(name='employee').exists():
				return self.employee_fieldsets
			if request.user.groups.filter(name='manager').exists():
				return self.manager_fieldsets
		else:
			return super(customuseradmin, self).get_fieldsets(request, obj)

	def get_queryset(self, request):
		if not request.user.is_superuser:
			if request.user.groups.filter(name='employee').exists():
				return User.objects.filter(email=request.user.email)
			if request.user.groups.filter(name='manager').exists():
				return User.objects.all()
		return User.objects.all()

class workadmin(admin.ModelAdmin):
 	list_display=('user','m_name','party_name','date','quantity',)
 	search_fields=('user__email','party_name','quantity',)
 	list_filter=('m_name',)
 	def get_queryset(self,request):
 		if not request.user.is_superuser:
 			if request.user.groups.filter(name='manager').exists():
 				return work.objects.all()
 			if request.user.groups.filter(name='employee').exists():
 				return work.objects.filter(user=request.user)
 		return work.objects.all()

class statusadmin(admin.ModelAdmin):
	list_display=('date','party_name','total','today',)
	search_fields=('party_name','remaining',)
	list_filter=('remaining',)
		
admin.site.register(User,customuseradmin)
admin.site.register(work,workadmin)

admin.site.register(status,statusadmin)

admin.site.site_title="work"
admin.site.index_title="User Dashboard"
admin.site.site_header="Work Analysis"
