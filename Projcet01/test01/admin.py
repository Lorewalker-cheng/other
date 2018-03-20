from django.contrib import admin
from test01.models import Department, Employee


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    # 指定后台网页要显示的字段
    list_display = ["id", "name", "create_date"]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'sex', 'salary', 'comment', 'department']


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
