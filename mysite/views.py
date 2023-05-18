from django.shortcuts import render, redirect
from django.http import  HttpResponse, HttpResponseRedirect
from mysite.models import Feedback
from mysite.models import Customer
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from mysite.models import Menu
from datetime import datetime
from .models import Attendance


def mysite(request):
    menu = Menu.objects.all()

    if request.method == 'POST':
        item1 = request.POST['item1']
        item2 = request.POST['item2']
        item3 = request.POST['item3']
        item4 = request.POST['item4']
        item5 = request.POST['item5']
        item6 = request.POST['item6']
        men = Menu(food1=item1, food2=item2, food3=item3, food4=item4, food5=item5, food6=item6)
        men.save()
        messages.success(request,'Menu added successfully.')
        return HttpResponseRedirect('/')
    if len(menu) >= 1:
        if int(str(datetime.now())[8:10]) == int(str(menu[0].timeStamp)[8:10]):
            return render(request,'mysite/home.html',{'menu':menu})
    return render(request,'mysite/home.html', {'menu':menu})
    

def about(request):
    return render(request,'mysite/about.html')


def feedback(request):
    if request.method =='POST':
        name =request.POST['name']
        phone =request.POST['phone']
        email =request.POST['email']
        address =request.POST['address']
        content =request.POST['content']
        print(name,phone,email,address,content)
        if len(name)<2 or len(phone)<10 or len(email)<5 or len(content) <4:
            messages.error(request,"Please fill the Form Correctly")
        else:
            feedback = Feedback(name= name,phone=phone,email=email,address=address,content=content)
            feedback.save()
            messages.success(request,"Thanks for Your Feedback")
    return render(request,'mysite/feedback.html')


    
def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Logged In')
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials Can't Login ")
            return redirect('home')
    return HttpResponse('/handlelogin')


def handlelogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return HttpResponseRedirect('/')
    

def customer(request):
    if request.method =='POST':
        fname = request.POST['fname']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        college = request.POST['college']
        year = request.POST['year']
        print(fname,phone,email,address,college,year)
        customer = Customer(fname=fname,phone=phone,email=email ,address=address, college=college,year=year)
        customer.save()
    return render(request,'mysite/form.html') 


def menu(request):
    return render(request,'mysite/home.html')


def deletemenu(request):
    menu = Menu.objects.all()
    menu[0].delete()
    messages.success(request, 'Menu deleted successfully')
    return HttpResponseRedirect('/')

def attendance(request):
    if request.method == 'POST':
        date_in =request.POST.get('date')
        sno = request.POST.get('sno')
        shift = request.POST.get('shift')
        print(date_in,sno,shift)
        att = Attendance(date_in=date_in,sno=sno,shift=shift)
        att.save()
    return render(request,'mysite/attendance.html')


def display(request):
    cus = Customer.objects.all
    return render(request,'mysite/admin_panel.html',{'cus':cus})

def deletecustomer(request):
    cus = Customer.objects.get(id)
    cus.delete()
    messages.success(request,'Customer deleted from the Record') 
    return render(request,'mysite/admin_panel.html')