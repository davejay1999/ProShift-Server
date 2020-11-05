from django.contrib import admin

from .models import *

# Register your models here.

class EmployeeStatusInline(admin.StackedInline):
    model = EmployeeRole
    can_delete = False
    verbose_name_plural = 'Employement'
    fk_name = 'user'
    extra = 0

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'company_code', 'phone')
    inlines = (EmployeeStatusInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('employee' , 'company' , 'start_date', 'is_approved', 'is_current')

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'is_manager')

class EmployeeRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'position')

admin.site.register(User, UserAdmin)
admin.site.register(Shift)
admin.site.register(Company)
admin.site.register(Position, PositionAdmin)
admin.site.register(EmployeeRole, EmployeeRoleAdmin)
admin.site.register(RequestedTimeOff)
admin.site.register(Availability, AvailabilityAdmin)
