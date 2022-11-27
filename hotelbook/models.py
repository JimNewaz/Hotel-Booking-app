from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Rooms(models.Model):   
    name = models.CharField(max_length=200, null=False)
    category = models.CharField(max_length=100, null=False)
    size = models.CharField(max_length=100, null=False)
    bedroom = models.CharField(max_length=100, null=True)
    washroom = models.CharField(max_length=100, null=True)
    balcony = models.CharField(max_length=100, null=True)
    reviews = models.CharField(max_length=100, default=None)
    price = models.CharField(max_length=100, null=True)
    allowance = models.IntegerField(null=False)
    roomNo = models.IntegerField(default=1)
    floor = models.IntegerField(default=1)
    description = models.CharField(max_length=500, null=False, default="Enter Your Room Details Here")
    image = models.ImageField(null=True,blank=True)
    

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return str(self.pk)

class RoomImage(models.Model):
    rooms = models.ForeignKey(Rooms, default=None, on_delete=models.CASCADE)
    images = models.FileField(null=True,blank=True)
 
    def __str__(self):
        return self.rooms.name

