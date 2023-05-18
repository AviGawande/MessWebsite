from django.db import models


class Feedback(models.Model):
    name =models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return 'Message from ' + self.name
    

    
class Customer(models.Model):
    
    sno =models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=200)
    college = models.CharField(max_length=120)
    year = models.CharField(max_length=50)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'New Registration from ' + self.fname





class Menu(models.Model):
    food1 = models.CharField(max_length=255)
    food2 = models.CharField(max_length=255)
    food3 = models.CharField(max_length=255)
    food4 = models.CharField(max_length=255)
    food5 = models.CharField(max_length=255)
    food6 = models.CharField(max_length=255)
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'Menu uploaded ' + self.food1


class Attendance(models.Model):
    date_in= models.DateField()
    sno = models.CharField(max_length=20)
    shift = models.CharField(max_length=50)
    timeStamp = models.DateTimeField( auto_now_add =True)

    def __str__(self):
        return 'attendance marked' + self.sno
        
    