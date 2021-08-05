from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from multiplex import models
from django.contrib.auth.models import User

@api_view(['POST'])
def occupy(request):
    if request.method=='POST':
        message=''
        movieid=request.data["movieid"]
        name=request.data["name"]
        date=request.data["date"]
        try:
            user = User.objects.create_user(name, name, name,first_name=name)
            user.save()
        except:
            user = User.objects.get(username=name)

        
        customer = models.Customer.objects.create(user=user)
        customer.save()
        seatnumber=request.data["seatnumber"]
        movie=None
        if int(movieid) > 0:
            try:
                movie = models.Movie.objects.get(id=movieid)
            except:
                if movie is None:
                    message='System Does Not Have Movie With This ID'
                    res={'message':message}
                    return Response(res)
                

            booking = models.Booking.objects.filter(movie=movie).filter(seatNumber=seatnumber).filter(date=date)
            if booking.exists():
                message='This Seat Already Occupied On This Date'
                res={'message':message}
                return Response(res)


            else:
                booking=models.Booking.objects.create(customer=customer,movie=movie,date=date,seatNumber=seatnumber,totalSeat='1',cost=100,watchers=name)
                booking.save()
                message='Seat Occupied'
                res={'message':message}
                return Response(res)


@api_view(['POST'])
def vacate(request):
    if request.method=='POST':
        message=''
        movieid=request.data["movieid"]
        seatnumber=request.data["seatnumber"]
        date=request.data["date"]
        
        movie=None
        if int(movieid) > 0:
            try:
                movie = models.Movie.objects.get(id=movieid)
            except:
                if movie is None:
                    message='System Does Not Have Movie With This ID'
                    res={'message':message}
                    return Response(res)
                

            booking = models.Booking.objects.filter(movie=movie).filter(seatNumber=seatnumber).filter(date=date)
            if booking.exists():
                for b in booking:
                    b.delete()
                message='Seat Vacated'
                res={'message':message}
                return Response(res)


            else:
                message='Seat Is Already Vacated'
                res={'message':message}
                return Response(res)


@api_view(['POST'])
def get_info(request):
    if request.method=='POST':
        message=''
        movieid=request.data["movieid"]
        seatnumber=request.data["seatnumber"]
        date=request.data["date"]
        
        movie=None
        if int(movieid) > 0:
            try:
                movie = models.Movie.objects.get(id=movieid)
            except:
                if movie is None:
                    message='System Does Not Have Movie With This ID'
                    res={'message':message}
                    return Response(res)
                

            booking = models.Booking.objects.filter(movie=movie).filter(seatNumber=seatnumber).filter(date=date)
            if booking.exists():
                seatnumber=None
                date=None
                totalcost=None
                customer=None
                bookingdate=None
                for b in booking:
                   seatnumber=b.seatNumber
                   moviedate=b.date
                   bookingdate=b.bookingDate
                   totalcost=b.cost
                   customer=b.customer

                message='Seat Occupied'
                res={'message':message,'seat_number':seatnumber,'total_cost':totalcost,'booking_date':bookingdate,'movie_date':moviedate}
                return Response(res)


            else:
                message='No Booking Found For This Details'
                res={'message':message}
                return Response(res)

 