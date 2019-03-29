from django.contrib import admin
from .models import *
admin.site.register(StaffDetails)
admin.site.register (Salary)
admin.site.register(Spend)
admin.site.register(Sundry)
admin.site.register(SalaryReportArchive)
admin.site.register(SundryReportArchive)
admin.site.register(ExpensesReportArchive)