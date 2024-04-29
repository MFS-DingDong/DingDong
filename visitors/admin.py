from django.contrib import admin

# Register your models here.
from .models import employee, visit

admin.site.register(employee)
admin.site.register(visit)