from django.urls import path
from sale import views


urlpatterns = [
    path('', views.index, name='index'),
    path('student', views.student, name='student'),
    path('about', views.about, name='about'),
    path('coupon', views.coupon, name='coupon'),
    path('blog', views.blog, name='blog'),
    path('metaTag', views.metaTag, name='metaTag'),
    
]
