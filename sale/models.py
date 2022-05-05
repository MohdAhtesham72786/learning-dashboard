from django.db import models

# Create your models here.
class Student(models.Model):
    membership_no = models.CharField(max_length=15)
    form_data = models.DateField()
    guardian_name = models.CharField(max_length=200)
    mothers_maiden_name = models.CharField(max_length=200)
    phone = models.BigIntegerField(unique=True)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    educational_qualification = models.CharField(max_length=50)
    membership_fee = models.IntegerField()
    share_count = models.IntegerField()
    introduced_by = models.CharField(max_length=15)  
    witness = models.CharField(max_length=250)


    
    
    

    



