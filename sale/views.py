from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse, JsonResponse
#from home.models import Contact
import os
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Student
from django.contrib.auth import authenticate,login
#Create your views here.

def index(request):
     return render(request,'myapp/index.html')

# store a student   
def student(request):
    if request.method=='POST':
        membership_no=request.POST['membership_no']
        form_no=request.POST['form_no']
        form_date=request.POST['form_date']
        name=request.POST['name']
        guardian_name=request.POST['guardian_name']
        mothers_maiden_name=request.POST['mothers_maiden_name']
        dob=request.POST['dob']
        phone=request.POST['phone']
        email=request.POST['email']
        gender=request.POST['gender']
        educational_qualification=request.POST['educational_qualification']
        membership_fee=request.POST['membership_fee']
        share_count=request.POST['share_count']
        introduced_by=request.POST['introduced_by']
        witness=request.POST['witness']
        
        '''ts=Student(membership_no=membership_no,form_no=form_no,form_date=form_date,name=name,guardian_name=guardian_name,mothers_maiden_name=mothers_maiden_name,
                    dob=dob,phone=phone,email=email,gender=gender,educational_qualification=educational_qualification,membership_fee=membership_fee,
                    share_count=share_count,introduced_by=introduced_by,witness=witness)
        ts.save()
        return HttpResponse('OK')
    else:
        #return HttpResponse('Password didnot match')
        return render(request,'sale/student.html')'''
        
        existingStudent = Student.objects.filter(phone=phone)
        if existingStudent.exists() :
            return JsonResponse({'status':"error","message":"Phone number already registered"},status=400)
              
        try :
            ts = Student(membership_no=membership_no,form_date=form_date,guardian_name=guardian_name,mothers_maiden_name=mothers_maiden_name,
                   phone=phone,email=email,gender=gender,educational_qualification=educational_qualification,membership_fee=membership_fee,
                   share_count=share_count,introduced_by=introduced_by,witness=witness)
            ts.save()
            return redirect('student')
        except Exception as e:
            errMessage = "Unable to save to db" + str(e)
            return JsonResponse({'status':"error","message": errMessage }, status=400)

    return render(request,'sale/student.html')