from django.urls import path

from . import views


urlpatterns = [
    path('', views.hotelbook, name="hotelbook"),
    path('about/', views.about, name="about"),
    path('booking/', views.booking, name="booking"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('room/', views.room, name="room"),
    path('amenities/', views.amenities, name="amenities")
]
