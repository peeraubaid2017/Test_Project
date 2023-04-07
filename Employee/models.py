from django.db import models

# Create your models here.
class EmployeeData(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=20)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    

    def __str__(self):
        return self.name
    
class Register(models.Model):
    eid = models.IntegerField()
    username=models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    is_on = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name
    
    



    