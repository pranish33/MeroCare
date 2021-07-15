from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils import timezone
from django.contrib import messages

# Create your views here.
#homepage 
def homepage(request):
	return render(request,'index.html')

def aboutpage(request):
	return render(request,'about.html')

#loginpage for different group user such as admin, doctor and patients
def loginpage(request):
	error = ""
	page = ""
	if request.method == 'POST':
		u = request.POST['email']
		p = request.POST['password']
		user = authenticate(request,username=u,password=p)
		try:
			if user is not None:
				login(request,user)
				error = "no"
				
				g = request.user.groups.all()[0].name
				if g == 'Doctor':
					page = "doctor"
					d = {'error': error,'page':page}
					return render(request,'doctorhome.html',d)
				
			
				elif g == 'Patient':
					page = "patient"
					d = {'error': error,'page':page}
					return render(request,'patienthome.html',d)

				elif g == 'Admin':
					page = "adminhome"
					d = {'error': error,'page':page}
					return render(request,'adminlogin.html',d)
			else:
				error = "yes"
				messages.info(request,'Invalid Credientials!')
				return redirect('loginpage')
		except Exception as e:
			error = "yes"
		
	return render(request,'login.html')

#creating account page for patients only 
def createaccountpage(request):
	error = ""
	user="none"
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']
		repeatpassword = request.POST['repeatpassword']
		gender = request.POST['gender']
		phonenumber = request.POST['phonenumber']
		
		try:
			if password == repeatpassword:
				Patient.objects.create(name=name,email=email,gender=gender,phonenumber=phonenumber)
				user = User.objects.create_user(first_name=name,email=email,password=password,username=email)
				pat_group = Group.objects.get(name='Patient')
				pat_group.user_set.add(user)
				
				user.save()
				
				error = "no"
				messages.info(request,'Account Created Sucessfully')
				return redirect('loginpage')
			else:
				error = "yes"
				messages.info(request,'Invalid Credientials!')
				return redirect('createaccountpage')
		except Exception as e:
			error = "yes"
			
	d = {'error' : error}
	
	return render(request,'createaccount.html',d)
	
#update Password 
def updatepassword(request):
	if request.method == 'POST':
		fm = PasswordChangeForm(user=request.user, data=request.POST)
		if fm.is_valid():
			fm.save()
			update_session_auth_hash(request, fm.user)
			return redirect('profile')
	
	fm = PasswordChangeForm(user=request.user)
	return render(request, 'updatepassword.html', {'form':fm})


#Doctor can only be added by admin 
def adminaddDoctor(request):
	error = ""
	user="none"
	if not request.user.is_staff:
		return redirect('login_admin')

	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']
		repeatpassword =  request.POST['repeatpasssword']
		gender = request.POST['gender']
		phonenumber = request.POST['phonenumber']
		address = request.POST['address']
		nmcnumber = request.POST['nmcnumber']
		specialization = request.POST['specialization']
		
		try:
			if password == repeatpassword:
				Doctor.objects.create(name=name,email=email,gender=gender,phonenumber=phonenumber,address=address,nmcnumber=nmcnumber,specialization=specialization)
				user = User.objects.create_user(first_name=name,email=email,password=password,username=email)
				doc_group = Group.objects.get(name='Doctor')
				doc_group.user_set.add(user)
				user.save()
				error = "no"
				messages.info(request,'Doctor Account Has been Created Sucessfully')
				return redirect('adminviewDoctor')
			else:
				error = "yes"
				
		except Exception as e:
			error = "yes"
	d = {'error' : error}
	return render(request,'adminadddoctor.html',d)

#admin can view added doctors 
def adminviewDoctor(request):
	if not request.user.is_staff:
		return redirect('login_admin')
	doc = Doctor.objects.all()
	d = { 'doc' : doc }
	return render(request,'adminviewDoctors.html',d)

#admin can delete doctor 
def admin_delete_doctor(request,pid,email):
	if not request.user.is_staff:
		return redirect('login_admin')
	doctor = Doctor.objects.get(id=pid)
	doctor.delete()
	users = User.objects.filter(username=email)
	users.delete()
	return redirect('adminviewDoctor')

#patients can delete appointment 
def patient_delete_appointment(request,pid):
	if not request.user.is_active:
		return redirect('loginpage')
	appointment = Appointment.objects.get(id=pid)
	appointment.delete()
	return redirect('viewappointments')



#admin can view appointment 	
def adminviewAppointment(request):
	if not request.user.is_staff:
		return redirect('login_admin')
	upcomming_appointments = Appointment.objects.filter(appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
	#print("Upcomming Appointment",upcomming_appointments)
	previous_appointments = Appointment.objects.filter(appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(status=False).order_by('-appointmentdate')
	#print("Previous Appointment",previous_appointments)
	d = { "upcomming_appointments" : upcomming_appointments, "previous_appointments" : previous_appointments }
	return render(request,'adminviewappointments.html',d)

#logout for doctor and patients 
def Logout(request):
	if not request.user.is_active:
		return redirect('loginpage')
	logout(request)
	return redirect('loginpage')

#logout function for admin
def Logout_admin(request):
	if not request.user.is_staff:
		return redirect('loginpage')
	logout(request)
	return redirect('loginpage')

def AdminHome(request):
	#after login user comes to this page.
	if not request.user.is_staff:
		return redirect('loginpage')
	return render(request,'adminhome.html')

def Home(request):
	if not request.user.is_active:
		return redirect('loginpage')

	g = request.user.groups.all()[0].name
	if g == 'Doctor':
		return render(request,'doctorhome.html')
	
	elif g == 'Patient':
		return render(request,'patienthome.html')
	elif g == 'Admin':
		return render(request,'adminhome.html')

#profile for doctor and patients
def profile(request):
	if not request.user.is_active:
		return redirect('loginpage')

	g = request.user.groups.all()[0].name
	if g == 'Patient':
		patient_detials = Patient.objects.all().filter(email=request.user)
		d = { 'patient_detials' : patient_detials }
		return render(request,'pateintprofile.html',d)
	elif g == 'Doctor':
		doctor_detials = Doctor.objects.all().filter(email=request.user)
		d = { 'doctor_detials' : doctor_detials }
		return render(request,'doctorprofile.html',d)
	
	

def MakeAppointments(request):
	error = ""
	if not request.user.is_active:
		return redirect('loginpage')
	#this gets all the doctors from database
	alldoctors = Doctor.objects.all()
	#this will send dectors to the template
	d = { 'alldoctors' : alldoctors }
	g = request.user.groups.all()[0].name
	if g == 'Patient':
		if request.method == 'POST':
			doctoremail = request.POST['doctoremail']
			doctorname = request.POST['doctorname']
			patientname = request.POST['patientname']
			patientemail = request.POST['patientemail']
			appointmentdate = request.POST['appointmentdate']
			symptoms = request.POST['symptoms']
			try:
				Appointment.objects.create(doctorname=doctorname,doctoremail=doctoremail,patientname=patientname,patientemail=patientemail,appointmentdate=appointmentdate,symptoms=symptoms,status=True,prescription="")
				error = "no"
				messages.info(request,'Appointment Booked Successfully!!')
				return redirect('makeappointments')
			except:
				error = "yes"
				messages.info(request,'Unable to Book appointment right now. Try Again Later')
				return redirect('makeappointments')
			e = {"error":error}
			return render(request,'pateintmakeappointments.html',e)
		elif request.method == 'GET':
			return render(request,'pateintmakeappointments.html',d)

def viewappointments(request):
	if not request.user.is_active:
		return redirect('loginpage')
	
	g = request.user.groups.all()[0].name
	if g == 'Patient':
		upcomming_appointments = Appointment.objects.filter(patientemail=request.user,appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
		
		previous_appointments = Appointment.objects.filter(patientemail=request.user,appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(patientemail=request.user,status=False).order_by('-appointmentdate')
		
		d = { "upcomming_appointments" : upcomming_appointments, "previous_appointments" : previous_appointments }
		return render(request,'patientviewappointments.html',d)
	elif g == 'Doctor':
		if request.method == 'POST':
			prescriptiondata = request.POST['prescription']
			followupdata = request.POST['followupdate']
			idvalue = request.POST['idofappointment']
			Appointment.objects.filter(id=idvalue).update(prescription=prescriptiondata,followupdate=followupdata,status=False)
			
		upcomming_appointments = Appointment.objects.filter(doctoremail=request.user,appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
		
		previous_appointments = Appointment.objects.filter(doctoremail=request.user,appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(doctoremail=request.user,status=False).order_by('-appointmentdate')
		
		d = { "upcomming_appointments" : upcomming_appointments, "previous_appointments" : previous_appointments }
		return render(request,'doctorviewappointment.html',d)

def viewhealthrecords(request):
	if not request.user.is_active:
		return redirect('loginpage')
	#print(request.user)
	g = request.user.groups.all()[0].name
	if g == 'Patient':
		upcomming_appointments = Appointment.objects.filter(patientemail=request.user,appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
		
		previous_appointments = Appointment.objects.filter(patientemail=request.user,appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(patientemail=request.user,status=False).order_by('-appointmentdate')
		
		d = { "upcomming_appointments" : upcomming_appointments, "previous_appointments" : previous_appointments }
		return render(request,'pateintviewrecord.html',d)
	elif g == 'Doctor':
		if request.method == 'POST':
			prescriptiondata = request.POST['prescription']
			followupdata = request.POST['followupdate']
			idvalue = request.POST['idofappointment']
			Appointment.objects.filter(id=idvalue).update(prescription=prescriptiondata,followupdate=followupdata,status=False)
			
		
		
		previous_appointments = Appointment.objects.filter(doctoremail=request.user,appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(doctoremail=request.user,status=False).order_by('-appointmentdate')
		
		d = { "upcomming_appointments" : upcomming_appointments, "previous_appointments" : previous_appointments }
		return render(request,'doctorviewappointment.html',d)
	
def contactus(request):
	error = ""
	if request.method == 'POST':
		contactname = request.POST['contactname']
		contactphonenumber = request.POST['contactphonenumber']
		contactemail = request.POST['contactemail']
		message = request.POST['message']
		contactus = Contact(contactname=contactname, contactemail=contactemail, contactphonenumber=contactphonenumber, message=message)
		contactus.save()
		error = "no"
		messages.info(request,'Your Messages has been recorded. We will Contact you soon!!')
	
		
		
	return render(request, 'contactus.html')
