from django.urls import path
from . import views



urlpatterns = [
    path('', views.mysite, name='home'),
    path('about/', views.about, name='about'),
    path('feedback', views.feedback, name='feedback'),
    path('login/', views.handlelogin, name='login'),
    path('customer', views.customer, name='customer'),
    path('handlelogout/', views.handlelogout, name='handlelogout'),
    path('menu',views.menu,name='menu'),
    path('deletemenu/', views.deletemenu, name='deletemenu'),
    path('attendance/',views.attendance,name='attendance'),
    path('display',views.display,name='display'),
    path('deletecustomer',views.deletecustomer,name='deletecustomer'),
    path('attendance/',views.attendance,name='attendance'),
]



