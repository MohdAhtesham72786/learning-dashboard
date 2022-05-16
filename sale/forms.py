from django import forms  
from .models import Coupon, Blog, MetaTag  
  
class CouponForm(forms.ModelForm):  
    class Meta:  
        model = Coupon  
        fields = "__all__"  
        
        
class BlogForm(forms.ModelForm):  
    class Meta:  
        model = Blog   
        fields = "__all__"  
        
        
class MetaTagForm(forms.ModelForm):  
    class Meta:  
        model = MetaTag  
        fields = "__all__"  