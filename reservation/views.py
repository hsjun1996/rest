from django.shortcuts import render, redirect,get_object_or_404
from django.utils import timezone
from .models import Reservation
from datetime import datetime, date
# Create your views here.
def reservation(request):
    return render(request, 'reservation.html')

def reservation_check(request): 
    reservations = Reservation.objects
    return render(request, 'reservation_check.html', {'reservations' : reservations})

def reservation_button(request):
        reservations = Reservation()
        reservations.userid = request.POST['userid']
        reservations.create_time = request.POST['date'] 
        reservations.people = request.POST['hopping_member']
        reservations.save()
        return redirect('reservation_check')

def reservation_delete(request, id):
    reservation = get_object_or_404(Reservation, pk=id)
    reservation.delete()
    return redirect('reservation_check')

def reservation_update(request, id):
    reservation = get_object_or_404(Reservation, pk=id)
    if request.method == 'GET':
        return render(request,'reservation_edit.html', {'reservation' : reservation})
    elif request.method == 'POST':
        userid = request.POST['userid']
        create_time = request.POST['date']
        people = request.POST['hopping_member']
        reservation.userid = userid
        reservation.create_time = create_time
        reservation.people = people
        reservation.save()
        return redirect("reservation_check")

    

