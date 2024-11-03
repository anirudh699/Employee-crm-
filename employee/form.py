from django import forms
from employee.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        
        widgets ={
        "name": forms.TextInput(attrs={"class": "form-control"}),
        "department": forms.TextInput(attrs={"class": "form-control"}),
        "gender": forms.Select(attrs={"class": "form-control form-select"}),
        "address": forms.Textarea(attrs={"class": "form-control"}),
        "salary": forms.TextInput(attrs={"class": "form-control"}),
        "email_id": forms.EmailInput(attrs={"class": "form-control"}),
        "mobile": forms.NumberInput(attrs={"class": "form-control"}),
        "date_of_joning": forms.TextInput(attrs={"class": "form-control","type":"date"}),
        "picture": forms.FileInput(attrs={"class": "form-control"}),
         }


        
    
   