from django import forms
from employee.models import Employee
from django.contrib.auth.models import User

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

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        
        fields=['username','email','password']
          
        widgets={
            'username':forms.TextInput(attrs={"class":"form-control"}),
            'email':forms.EmailInput(attrs={"class":"form-control"}),
            'password':forms.PasswordInput(attrs={"class":"form-control"}),
        }

class SignInForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control "}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
        
          
       
      
    
        
    
   