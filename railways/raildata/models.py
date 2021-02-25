from django.db import models

# Create your models here.

class UserDetails(models.Model):
    # fullname=models.CharField(max_length=50)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=50)
    conf_pass=models.CharField(max_length=50)
    id = models.AutoField(primary_key="id")
    age=models.DateField()
    contact=models.IntegerField()
    gender=models.CharField(max_length=5)

class Passenger(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    passsword=models.CharField(max_length=30)

class Admin(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=30)


class Train(models.Model):
    Trainno=models.IntegerField(primary_key=True)
    Trainname=models.CharField(max_length=50)
    Source=models.CharField(max_length=30)
    Destination=models.CharField(max_length=30)

class Reservation(models.Model):
    noOfPassenger=models.IntegerField()
    Age=models.IntegerField()
    Gender=models.CharField(max_length=1)

class Tickets(models.Model):
    Ticketno=models.IntegerField(primary_key=True)
    Source=models.CharField(max_length=30)
    Destination=models.CharField(max_length=30)
    ticketStatus=models.CharField(max_length=10)

class Payment(models.Model):
    Amount=models.IntegerField()
    