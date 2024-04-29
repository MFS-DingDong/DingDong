from django.db import models

# Create your models here.
class employee(models.Model):
    """Current Employees Name and email address"""
    employee_name = models.CharField(max_length=200)
    employee_email = models.EmailField(max_length=200)

    def __str__(self):
        return self.employee_name

class visit(models.Model):
    """Form to be filled out by Visitors"""
    visitor_name = models.CharField(max_length=200)
    reason_for_visit = models.TextField()
    Employee_Name = models.ForeignKey(employee, on_delete=models.CASCADE)