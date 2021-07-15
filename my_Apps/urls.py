from django.contrib import admin
from django.urls import path
#from my_Apps.views import *
from .import chatbotviews
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('',views.homepage,name='homepage'),
    path('about/',views.aboutpage,name='aboutpage'),
    path('login/',views.loginpage,name='loginpage'),
    path('createaccount',views.createaccountpage,name='createaccountpage'),
    path('adminhome/',views.AdminHome,name='adminhome'),
    path('adminlogout/',views.Logout_admin,name='adminlogout'),
    path('adminaddDoctor/',views.adminaddDoctor,name='adminaddDoctor'),
    path('adminviewDoctor/',views.adminviewDoctor,name='adminviewDoctor'),
    path('adminDeleteDoctor<int:pid><str:email>',views.admin_delete_doctor,name='admin_delete_doctor'),
    path('chatroom/', chatbotviews.chatroom, name= 'chatroom'),
    path('adminviewAppointment/',views.adminviewAppointment,name='adminviewAppointment'),
    path('home/',views.Home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('updatepassword/',views.updatepassword,name='updatepassword'),
    path('makeappointments/',views.MakeAppointments,name='makeappointments'),
    path('viewappointments/',views.viewappointments,name='viewappointments'),
    path('viewhealthrecords/',views.viewhealthrecords,name='viewhealthrecords'),
    path('contact/',views.contactus,name='contactus'),
    path('PatientDeleteAppointment<int:pid>',views.patient_delete_appointment,name='patient_delete_appointment'),
   
    path('logout/',views.Logout,name='logout'),
    #For Forgot Password and Reset Password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='forgot.html'), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='reset.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='passwordresetcomplete.html'), name="password_reset_complete"),

    

]