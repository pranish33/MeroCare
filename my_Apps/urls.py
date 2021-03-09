from django.contrib import admin
from django.urls import path
#from my_Apps.views import *
from .import chatbotviews
from . import views


urlpatterns = [
    
    path('',views.homepage,name='homepage'),
    path('about/',views.aboutpage,name='aboutpage'),
    path('login/',views.loginpage,name='loginpage'),
    path('createaccount',views.createaccountpage,name='createaccountpage'),
    path('admin_login/',views.Login_admin,name='login_admin'),
    path('adminhome/',views.AdminHome,name='adminhome'),
    path('adminlogout/',views.Logout_admin,name='adminlogout'),
    path('adminaddDoctor/',views.adminaddDoctor,name='adminaddDoctor'),
    path('adminviewDoctor/',views.adminviewDoctor,name='adminviewDoctor'),
    path('adminDeleteDoctor<int:pid><str:email>',views.admin_delete_doctor,name='admin_delete_doctor'),
    path('chatroom/', chatbotviews.chatroom, name= 'chatroom'),
    path('adminviewAppointment/',views.adminviewAppointment,name='adminviewAppointment'),
    path('home/',views.Home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('makeappointments/',views.MakeAppointments,name='makeappointments'),
    path('viewappointments/',views.viewappointments,name='viewappointments'),
    path('PatientDeleteAppointment<int:pid>',views.patient_delete_appointment,name='patient_delete_appointment'),
    path('logout/',views.Logout,name='logout'),
]