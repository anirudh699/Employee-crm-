from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    gender_option={
        ("male","male"),
        ("female","female")
    }
    gender=models.CharField(max_length=200,choices=gender_option,default="male")
    
    address=models.TextField()
    
    salary=models.PositiveIntegerField()
    
    email_id=models.EmailField()
    
    mobile=models.PositiveIntegerField()
    
    date_of_joning=models.DateField(null=True)
    
    picture=models.ImageField(upload_to="employee_image",null=True)

    def __str__(self):
        return self.name
   