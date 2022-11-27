from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.http import HttpResponse
from .models import * 

# Create your views here.
def hotelbook(request):
    rooms = Rooms.objects.all()
    photos = RoomImage.objects.all()
    context = {'rooms':rooms, 'photos':photos} 
    return render(request, 'hotelbook/index.html', context)

def about(request):
    context = {}
    return render(request, 'hotelbook/about.html', context)

def booking(request):
    context = {}
    return render(request, 'hotelbook/booking.html', context)

def contact(request):
    context = {}
    return render(request, 'hotelbook/contact.html', context)

def register(request):    

    if request.method == 'POST':
        uname = request.POST.get('uname')
        uemail = request.POST.get('uemail')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(uname, uemail, password)
        new_user.save()
        return redirect('login')

    context = {}
    return render(request, 'hotelbook/register.html', context)

def login(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        
        user = authenticate(request, username=uname, password=upass)
        print(user)
        if user is not None:
            auth_login(request, user)            
            return redirect('hotelbook')
        else:           
            return HttpResponse("User is not registered")
    
    context = {}
    return render(request, 'hotelbook/login.html', context)


def userlogout(request):
    logout(request)
    return redirect('login')

def room(request):
    rooms = Rooms.objects.all()
    photos = RoomImage.objects.all()
    context = {'rooms':rooms, 'photos':photos}    
    return render(request, 'hotelbook/room.html', context)

def amenities(request):
    context = {}
    return render(request, 'hotelbook/amenities.html', context)
