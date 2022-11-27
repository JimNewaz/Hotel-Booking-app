from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
# admin.site.register(Rooms)


class RoomImageAdmin(admin.StackedInline):
    model = RoomImage

@admin.register(Rooms)
class PostAdmin(admin.ModelAdmin):
    inlines = [RoomImageAdmin]
 
    class Meta:
       model = Rooms

@admin.register(RoomImage)
class RoomImageAdmin(admin.ModelAdmin):
    pass