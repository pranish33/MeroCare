from django.shortcuts import render

# Create your views here.

def chatroom(request):
    return render(request, 'chatroom.html')
