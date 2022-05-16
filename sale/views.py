from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse, JsonResponse
import os
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Student,Coupon,Blog,MetaTag
from .forms import Coupon,Blog,MetaTagForm
from django.contrib.auth import authenticate,login add 
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
        
        existingStudent = Student.objects.filter(membership_no=membership_no,form_no=form_no,form_date=form_date,name=name,guardian_name=guardian_name,mothers_maiden_name=mothers_maiden_name,
                        dob=dob,phone=phone,email=email,gender=gender,educational_qualification=educational_qualification,membership_fee=membership_fee,
                        share_count=share_count,introduced_by=introduced_by,witness=witness)
        if existingStudent.exists() :
            return JsonResponse({'status':"error","message":"membership_no,form_no,form_date,name,guardian_name,mothers_maiden_name,dob,phone,email,gender,educational_qualification,membership_fee,share_count,introduced_by,witness already registered"},status=400)
              
        try :
            ts = Student(membership_no=membership_no,form_no=form_no,form_date=form_date,name=name,guardian_name=guardian_name,mothers_maiden_name=mothers_maiden_name,
                        dob=dob,phone=phone,email=email,gender=gender,educational_qualification=educational_qualification,membership_fee=membership_fee,
                        share_count=share_count,introduced_by=introduced_by,witness=witness)
            ts.save()
            return redirect('student')
        except Exception as e:
            errMessage = "Unable to save to db" + str(e)
            return JsonResponse({'status':"error","message": errMessage }, status=400)
    
    return render(request,'sale/student.html')


def about(request):
    student = Student.objects.all()
    return render(request,'sale/about.html',{'student':student})



def coupon(request):  
    if request.method == "POST":  
        form = CouponForm(request.POST)  
        if form.is_valid():
            code = form.cleaned_data['code']
            description = form.cleaned_data['description']
            amount = form.cleaned_data['amount']
            amount_type = form.cleaned_data['amount_type']
            print('code',form.cleaned_data['code'])
            print('description',form.cleaned_data['code'])
            print('amount',form.cleaned_data['code'])
            print('amount_type',form.cleaned_data['amount_type'])  
            try:  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = CouponForm()  
    return render(request,'sale/coupon.html',{'form':form})  



def blog(request):  
    if request.method == "POST":  
        form = BlogForm(request.POST)  
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            tags = form.cleaned_data['tags']
            body = form.cleaned_data['body']
            date_time = form.cleaned_data['date_time'] 
            print('title',form.cleaned_data['title'])
            print('image',form.cleaned_data['image'])
            print('tags',form.cleaned_data['tags'])
            print('body',form.cleaned_data['body'])
            print('date_time',form.cleaned_data['date_time']) 
            try:  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = BlogForm()  
    return render(request,'sale/blog.html',{'form':form})  

def metaTag(request):  
    if request.method == "POST":  
        form = MetaTagForm(request.POST)  
        if form.is_valid():
            cupon = form.cleaned_data['cupon']
            blog = form.cleaned_data['blog']
            print('cupon',form.cleaned_data['cupon'])
            print('blog',form.cleaned_data['blog'])  
            try:  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = MetaTagForm()  
    return render(request,'sale/metaTag.html',{'form':form})  

