from django.db import models

# Create your models here.
class Student(models.Model):
    membership_no = models.CharField(max_length=15)
    form_no = models.CharField(max_length=20,default=0)
    form_date = models.DateField(null=True)
    name = models.CharField(max_length=200,default=0)
    guardian_name = models.CharField(max_length=200)
    mothers_maiden_name = models.CharField(max_length=200)
    dob = models.DateField(null=True,default=0)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    educational_qualification = models.CharField(max_length=50)
    membership_fee = models.IntegerField()
    share_count = models.IntegerField()
    introduced_by = models.CharField(max_length=15)  
    witness = models.CharField(max_length=250)
    
    
class Coupon(models.Model):
    code = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    amount_type = models.CharField(max_length=255, default='Percentage')

    class Meta:
        verbose_name_plural = "Coupons"
        
        
class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blog_image")
    tags = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    date_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Blogs"


class MetaTag(models.Model):
    cupon = models.ForeignKey(Coupon, null=True, blank=True, on_delete=models.DO_NOTHING)
    blog = models.ForeignKey(Blog, null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Meta Tags"


    
    
    

    



