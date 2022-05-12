from django.db import models

# Create your models here.
class Student(models.Model):
    membership_no = models.CharField(max_length=15)
    form_no = models.CharField(max_length=20,default=0)
    form_date = models.DateField(null=True)
    name = models.CharField(max_length=200,default='')
    guardian_name = models.CharField(max_length=200)
    mothers_maiden_name = models.CharField(max_length=200)
    dob = models.DateField(null=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    educational_qualification = models.CharField(max_length=50)
    membership_fee = models.IntegerField()
    share_count = models.IntegerField()
    introduced_by = models.CharField(max_length=15)  
    witness = models.CharField(max_length=250)


    
    
    

    



