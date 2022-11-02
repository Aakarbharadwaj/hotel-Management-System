from asyncio.windows_events import NULL
from django.db import models


# Create your models here.
class Details(models.Model):
    id = models.BigAutoField(primary_key=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Adhar_id = models.CharField(max_length=50)
    Room_no = models.CharField(max_length=50)
    Time_in = models.DateTimeField(auto_now=True)
    Time_Out = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    Contact = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Details'

    def __str__(self):
        return self.First_Name


class guestDetails(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    idtype = models.CharField(max_length=50)
    idnumber = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'guestDetails'

    def __str__(self):
        return self.firstName


class Rooms(models.Model):
    room_number = models.CharField(max_length=50)
    room_size = models.CharField(max_length=50)
    room_type = models.CharField(max_length=50)
    room_price = models.CharField(max_length=50)
    reserved_room = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return f'{self.room_number} is {self.room_size} and {self.room_type} ,price ={self.room_price}'

class Bookings(models.Model):
    Guest = models.ForeignKey(guestDetails,on_delete= models.DO_NOTHING)
    Room = models.ForeignKey(Rooms,on_delete=models.DO_NOTHING)
    number_of_people = models.CharField(max_length=50)
    checkin_datetime = models.DateTimeField(auto_now_add=True)
    checkout_datetime = models.DateTimeField(null=True)
    amount = models.CharField(max_length=50)