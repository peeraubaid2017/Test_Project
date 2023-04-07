from django import forms
from .models import Employee

class employee_data_Form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
    