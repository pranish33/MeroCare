from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Doctor(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	nmcnumber = models.CharField(max_length=10)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	
	bloodgroup = models.CharField(max_length=5)
	specialization = models.CharField(max_length=50)
	

	def __str__(self):
		return self.name


class Patient(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	#created_at=models.DateTimeField(auto_now_add=True)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	bloodgroup = models.CharField(max_length=5)

	def __str__(self):
		return self.name
	
	

class Appointment(models.Model):
	doctorname = models.CharField(max_length=50)
	doctoremail = models.EmailField(max_length=50)
	patientname = models.CharField(max_length=50)
	patientemail = models.EmailField(max_length=50)
	appointmentdate = models.DateField(max_length=10)
	followupdate = models.DateField(max_length=10)
	symptoms = models.CharField(max_length=100)
	status = models.BooleanField()
	prescription = models.CharField(max_length=200)

	
	
	def __str__(self):
		return self.patientname+" you have appointment with "+self.doctorname