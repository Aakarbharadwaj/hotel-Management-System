import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Details, guestDetails, Bookings, Rooms


# Create your views here.

def visitorDetails(request):
    First_Name = request.POST.get('fname')
    Last_Name = request.POST.get('lname')
    Address = request.POST.get('add')
    Adhar_id = request.POST.get('adhar')
    Room_no = request.POST.get('room')
    Contact = request.POST.get('contact')

    if not First_Name or not Last_Name or not Address or not Adhar_id or not Room_no or not Contact:
        return HttpResponse('All fields are mandatory')

    data = Details.objects.filter(First_Name=First_Name, Last_Name=Last_Name, Address=Address, Adhar_id=Adhar_id,
                                  Room_no=Room_no, Contact=Contact)

    for ele in data:
        if ele.Adhar_id == Adhar_id:
            fdata = Details(First_Name=First_Name, Last_Name=Last_Name, Address=Address, Adhar_id=Adhar_id,
                            Room_no=Room_no, Contact=Contact)
            fdata.save()
            return HttpResponse(f"visitor has visited before on  {ele.Time_in}")
    fdata = Details(First_Name=First_Name, Last_Name=Last_Name, Address=Address, Adhar_id=Adhar_id,
                    Room_no=Room_no, Contact=Contact)
    fdata.save()
    return HttpResponse('entry saved')


def visitorOut(request):
    Contact = request.POST.get('contact')

    if not Contact:
        return HttpResponse('enter contact')

    data = Details.objects.filter(Contact=Contact, Time_Out__isnull=True)
    print()
    print(data[0])
    print('yes')
    # update = datetime.datetime.now()
    data[0].Time_Out = datetime.datetime.now()
    # data[0].First_Name = 'Aakar'
    print(data[0].Time_Out)
    # print(update)
    data[0].save()

    return HttpResponse('checked_out')


def addGuest(request):
    if request.method == "POST":
        firstName = request.POST.get('fname')
        lastName = request.POST.get('lname')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        idtype = request.POST.get('idtype')
        idnumber = request.POST.get('idnumber')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        if not firstName or not lastName or not contact or not email or not idtype or not idnumber or not address \
                or not city or not state:
            return HttpResponse("enter all fields")
        data = guestDetails(firstName=firstName, lastName=lastName, contact=contact, email=email, idtype=idtype,
                            idnumber=idnumber,
                            address=address, city=city, state=state)
        data.save()
        return HttpResponse("data saved")


def currentGuest(request):
    if request.method == "POST":
        data = Bookings.objects.filter(checkout_datetime__isnull == True)
        l = []
        for ele in data:
            Guest_object = guestDetails.objects.get(id=ele.Guest_id)
            Room_object = Rooms.objects.get(id=ele.Room_id)
            l.append({'name': Guest_object.firstName, 'roomName': Room_object.room_number, 'people': ele.number_of_people,
                      'checkinTime':ele.checkin_datetime})
            d = {'info': l}
            return JsonResponse(d)


