from django.shortcuts import render,redirect
from django.views.generic import View

from employee.form import EmployeeForm,SignUpForm,SignInForm
from employee.models import Employee 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from employee.decorators import signin_required



# Create your views here.
@method_decorator(signin_required,name="dispatch")
class EmployeeCreateView(View):
    template_name="employee_add.html"
    form_class=EmployeeForm
    
    def get(self,request,*args,**kwrgs):
        form_instance=self.form_class
    
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        
        form_instance=self.form_class(form_data,files=request.FILES) 
        
        if form_instance.is_valid():
            
            form_instance.save()
            messages.success(request,"Employee sucessfulyy added")
            
            
            return redirect("employee-list")
        messages.error(request,"Failed to add Employee!!")
        return render(request,self.template_name,{"form":form_instance})
            
@method_decorator(signin_required,name="dispatch")        
class EmployeeListView(View):
    template_name="employee_list.html"
    
    def get(self,request,*args,**kwargs):
        
        qs=Employee.objects.all()
        
        return render(request,self.template_name,{"data":qs})
        
@method_decorator(signin_required,name="dispatch")
class EmployeeDetailView(View):
    template_name="employee_detail.html"
    
    
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        
        qs=Employee.objects.get(id=id)
        
        return render(request,self.template_name,{"data":qs})
@method_decorator(signin_required,name="dispatch")
class EmployeeDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        Employee.objects.get(id=id).delete()
        messages.success(request,"Deleted")
        
        return redirect("employee-list")
@method_decorator(signin_required,name="dispatch")   
class EmployeeUpdateView(View):
    template_name="employee_update.html"
    form_class=EmployeeForm
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        
        employee_object=Employee.objects.get(id=id)
        
        form_instance=self.form_class(instance=employee_object)
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        
        employee_object=Employee.objects.get(id=id)
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data,files=request.FILES,instance=employee_object)
        
        if form_instance.is_valid():
            form_instance.save()
            
            messages.success(request,"Sucessfully Updated employe")
            
            return redirect("employee-list")
        messages.error(request,"Failed to Update")
        return render(request,self.template_name,{"form":form_instance})

class EmployeeSignUpView(View):
    template_name="employee_reg.html"
    
    form_class=SignUpForm
        
    def get(self,request,*args,**kwrgs):
    
        form_instance=self.form_class()
    
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
    
        form_data=request.POST
        
        form_instance=self.form_class(form_data) 
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            User.objects.create_user(**data)
            
           

            return redirect("register")
        
        return render(request,self.template_name,{"form":form_instance})
            
class SigninView(View):
    template_name="signIn.html"
    form_class=SignInForm
    
    def get(self,request,*args,**kwargs):
       
        form_instance=self.form_class()
       
        return render(request,self.template_name,{"form":form_instance})
        
    def post (self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance =self.form_class(form_data    )
        
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            
            usname=data.get('username')
            pwd=data.get('password')
            
            
            user_obj=authenticate(request,username=usname,password=pwd)
            
            if user_obj:
                login(request,user_obj)
            
            return redirect('employee-list')   
        
        
        return render(request,self.template_name,{"form":form_instance}) 
@method_decorator(signin_required,name="dispatch")
class SignoutView(View):
    def get(self,request,*args,**kwargs):
        
        logout(request)
        messages.success(request,"singedout")
        return redirect ('signin')          
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        
        