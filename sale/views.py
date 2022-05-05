from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
#from home.models import Contact
import os
from django.contrib import messages
from django.contrib.auth.models import User
#from .models import Student
from django.contrib.auth import authenticate,login
#Create your views here.

def index(request):
     return render(request,'myapp/index.html')

# store a student   
def student(request):
    if request.method=='POST':
        membership_no=request.POST['membership_no']
        form_data=request.POST['form_data']
        guardian_name=request.POST['guardian_name']
        mothers_maiden_name=request.POST[' mothers_maiden_name']
        phone=request.POST['phone']
        email=request.POST['email']
        gender=request.POST['gender']
        educational_qualification=request.POST['educational_qualification']
        membership_fee=request.POST.get['membership_fee']
        share_count=request.POST['share_count']
        introduced_by=request.POST['introduced_by']
        witness=request.POST['witness']
        ts=Student(membership_no=membership_no,form_data=form_data,guardian_name=guardian_name, mothers_maiden_name= mothers_maiden_name,
                   phone= phone,email=email,gender=gender,educational_qualification=educational_qualification,membership_fee=membership_fee,
                   share_count=share_count,introduced_by=introduced_by,witness=witness)
        ts.save()
    else:
        #return HttpResponse('Password didnot match')
        return render(request,'sale/student.html')