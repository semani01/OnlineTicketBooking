from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    movies=models.Movie.objects.all()
    return render(request,'multiplex/index.html',{'movies':movies})


#for showing signup/login button for customer
def customerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'multiplex/customerclick.html')

#for showing signup/login button for producer
def producerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'multiplex/producerclick.html')

#for showing signup/login button for distributor
def distributorclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'multiplex/distributorclick.html')

#for showing signup/login button for theatre
def theatreclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'multiplex/theatreclick.html')


#for showing signup/login button for ADMIN(by sumit)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')

def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request,'multiplex/customersignup.html',context=mydict)

def producer_signup_view(request):
    userForm=forms.ProducerUserForm()
    producerForm=forms.ProducerForm()
    mydict={'userForm':userForm,'producerForm':producerForm}
    if request.method=='POST':
        userForm=forms.ProducerUserForm(request.POST)
        producerForm=forms.ProducerForm(request.POST,request.FILES)
        if userForm.is_valid() and producerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            producer=producerForm.save(commit=False)
            producer.user=user
            producer.save()
            my_producer_group = Group.objects.get_or_create(name='PRODUCER')
            my_producer_group[0].user_set.add(user)
        return HttpResponseRedirect('producerlogin')
    return render(request,'multiplex/producersignup.html',context=mydict)

def distributor_signup_view(request):
    userForm=forms.DistributorUserForm()
    distributorForm=forms.DistributorForm()
    mydict={'userForm':userForm,'distributorForm':distributorForm}
    if request.method=='POST':
        userForm=forms.DistributorUserForm(request.POST)
        distributorForm=forms.DistributorForm(request.POST,request.FILES)
        if userForm.is_valid() and distributorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            distributor=distributorForm.save(commit=False)
            distributor.user=user
            distributor.save()
            my_distributor_group = Group.objects.get_or_create(name='DISTRIBUTOR')
            my_distributor_group[0].user_set.add(user)
        return HttpResponseRedirect('distributorlogin')
    return render(request,'multiplex/distributorsignup.html',context=mydict)

def theatre_signup_view(request):
    userForm=forms.TheatreUserForm()
    theatreForm=forms.TheatreForm()
    mydict={'userForm':userForm,'theatreForm':theatreForm}
    if request.method=='POST':
        userForm=forms.TheatreUserForm(request.POST)
        theatreForm=forms.TheatreForm(request.POST,request.FILES)
        if userForm.is_valid() and theatreForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            theatre=theatreForm.save(commit=False)
            theatre.user=user
            theatre.save()
            my_theatre_group = Group.objects.get_or_create(name='THEATRE')
            my_theatre_group[0].user_set.add(user)
        return HttpResponseRedirect('theatrelogin')
    return render(request,'multiplex/theatresignup.html',context=mydict)




#for checking user customer
def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

#for checking user is producer
def is_producer(user):
    return user.groups.filter(name='PRODUCER').exists()

#for checking user is distributor
def is_distributor(user):
    return user.groups.filter(name='DISTRIBUTOR').exists()

#for checking user is theatre owner
def is_theatre(user):
    return user.groups.filter(name='THEATRE').exists()


def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('customer-home')
    elif is_producer(request.user):
        accountapproval=models.Producer.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('producer-dashboard')
        else:
            return render(request,'multiplex/wait_for_account_approval.html')

    elif is_distributor(request.user):
        accountapproval=models.Distributor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('distributor-dashboard')
        else:
            return render(request,'multiplex/wait_for_account_approval.html')

    elif is_theatre(request.user):
        accountapproval=models.Theatre.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('theatre-dashboard')
        else:
            return render(request,'multiplex/wait_for_account_approval.html')

    else:
        return redirect('admin-dashboard')


#============================================================================================
# ADMIN RELATED views start
#============================================================================================
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    dict={
    'total_customer':models.Customer.objects.all().count(),
    'total_producer':models.Producer.objects.filter(status=True).count(),
    'total_distributor':models.Distributor.objects.filter(status=True).count(),
    'total_theatre':models.Theatre.objects.filter(status=True).count(),
    }
    return render(request,'multiplex/admin_dashboard.html',context=dict)

@login_required(login_url='adminlogin')
def admin_movie_view(request):
    return render(request,'multiplex/admin_movie.html')


@login_required(login_url='adminlogin')
def admin_add_movie_view(request):
    theatreForm=forms.AdminTheatreForm()
    if request.method=='POST':
        theatreForm=forms.AdminTheatreForm(request.POST)
        movie=models.Movie()
        if theatreForm.is_valid():
            movie.theatre=theatreForm.cleaned_data['theatre']
        movie.name=request.POST['name']
        movie.actor=request.POST['actorname']
        movie.director=request.POST['directorname']
        movie.description=request.POST['description']
        movie.release_date=request.POST['release_date']
        movie.out_date=request.POST['out_date']
        movie.poster=request.FILES['poster']
        movie.video=request.POST['video']

        movie.save()


        #for making seat available between release date and out_date
        start_date = request.POST['release_date']
        start_date=date(int(start_date[0:4]),int(start_date[5:7]),int(start_date[8:10]))
        end_date = request.POST['out_date']
        end_date=date(int(end_date[0:4]),int(end_date[5:7]),int(end_date[8:10]))
        delta = timedelta(days=1)
        moviex=models.Movie.objects.get(id=movie.id)
        while start_date <= end_date:
            seat=models.Seat(movie=moviex,date=start_date)
            seat.save()
            start_date += delta


        return HttpResponseRedirect('admin-movie')
    return render(request,'multiplex/admin_add_movie.html',{'theatreForm':theatreForm})


@login_required(login_url='adminlogin')
def admin_customer_view(request):
    return render(request,'multiplex/admin_customer.html')

@login_required(login_url='adminlogin')
def admin_view_customer_view(request):
    customers=models.Customer.objects.all()
    return render(request,'multiplex/admin_view_customer.html',{'customers':customers})

@login_required(login_url='adminlogin')
def delete_customer_view(request,pk):
    customer=models.Customer.objects.get(id=pk)
    user=models.User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return HttpResponseRedirect('/admin-view-customer')


@login_required(login_url='adminlogin')
def admin_add_customer_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('/admin-view-customer')
    return render(request,'multiplex/admin_add_customer.html',context=mydict)


@login_required(login_url='adminlogin')
def admin_view_customer_booking_view(request):
    bookings=models.Booking.objects.all()
    return render(request,'multiplex/admin_view_customer_booking.html',{'bookings':bookings})

@login_required(login_url='adminlogin')
def delete_booking_view(request,pk):
    booking=models.Booking.objects.get(id=pk)
    booking.delete()
    return HttpResponseRedirect('/admin-view-customer-booking')


def cancel_ticket_view(request,pk):
    booking=models.Booking.objects.get(id=pk)
    booking.delete()
    return HttpResponseRedirect('/customer-ticket')




@login_required(login_url='adminlogin')
def admin_view_movie_view(request):
    movies=models.Movie.objects.all()
    return render(request,'multiplex/admin_view_movie.html',{'movies':movies})

@login_required(login_url='adminlogin')
def delete_movie_view(request,pk):
    movie=models.Movie.objects.get(id=pk)
    movie.delete()
    return HttpResponseRedirect('/admin-view-movie')

@login_required(login_url='adminlogin')
def admin_view_released_movie_view(request):
    movies=models.Movie.objects.all()
    return render(request,'multiplex/admin_view_released_movie.html',{'movies':movies})

@login_required(login_url='adminlogin')
def admin_view_not_released_movie_view(request):
    movies=models.TempMovie.objects.filter(theatre_status='Movie Not Released')
    return render(request,'multiplex/admin_view_not_released_movie.html',{'movies':movies})




@login_required(login_url='adminlogin')
def admin_view_producer_view(request):
    producers=models.Producer.objects.filter(status=True)
    return render(request,'multiplex/admin_view_producer.html',{'producers':producers})

@login_required(login_url='adminlogin')
def admin_add_producer_view(request):
    userForm=forms.ProducerUserForm()
    producerForm=forms.ProducerForm()
    mydict={'userForm':userForm,'producerForm':producerForm}
    if request.method=='POST':
        userForm=forms.ProducerUserForm(request.POST)
        producerForm=forms.ProducerForm(request.POST,request.FILES)
        if userForm.is_valid() and producerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            producer=producerForm.save(commit=False)
            producer.user=user
            producer.status=True
            producer.save()
            my_producer_group = Group.objects.get_or_create(name='PRODUCER')
            my_producer_group[0].user_set.add(user)
        return HttpResponseRedirect('admin-view-producer')
    return render(request,'multiplex/admin_add_producer.html',context=mydict)


@login_required(login_url='adminlogin')
def delete_producer_view(request,pk):
    producer=models.Producer.objects.get(id=pk)
    user=models.User.objects.get(id=producer.user_id)
    user.delete()
    producer.delete()
    return HttpResponseRedirect('/admin-view-producer')

@login_required(login_url='adminlogin')
def admin_view_producer_movie_view(request):
    movies=models.TempMovie.objects.all()
    return render(request,'multiplex/admin_view_producer_movie.html',{'movies':movies})







@login_required(login_url='adminlogin')
def admin_view_distributor_view(request):
    distributors=models.Distributor.objects.filter(status=True)
    return render(request,'multiplex/admin_view_distributor.html',{'distributors':distributors})

@login_required(login_url='adminlogin')
def delete_distributor_view(request,pk):
    distributor=models.Distributor.objects.get(id=pk)
    user=models.User.objects.get(id=distributor.user_id)
    user.delete()
    distributor.delete()
    return HttpResponseRedirect('/admin-view-distributor')

@login_required(login_url='adminlogin')
def admin_add_distributor_view(request):
    userForm=forms.DistributorUserForm()
    distributorForm=forms.DistributorForm()
    mydict={'userForm':userForm,'distributorForm':distributorForm}
    if request.method=='POST':
        userForm=forms.DistributorUserForm(request.POST)
        distributorForm=forms.DistributorForm(request.POST,request.FILES)
        if userForm.is_valid() and distributorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            distributor=distributorForm.save(commit=False)
            distributor.user=user
            distributor.status=True
            distributor.save()
            my_distributor_group = Group.objects.get_or_create(name='DISTRIBUTOR')
            my_distributor_group[0].user_set.add(user)
        return HttpResponseRedirect('admin-view-distributor')
    return render(request,'multiplex/admin-add-distributor.html',context=mydict)

@login_required(login_url='adminlogin')
def admin_view_theatre_view(request):
    theatres=models.Theatre.objects.filter(status=True)
    return render(request,'multiplex/admin_view_theatre.html',{'theatres':theatres})

@login_required(login_url='adminlogin')
def delete_theatre_view(request,pk):
    theatre=models.Theatre.objects.get(id=pk)
    user=models.User.objects.get(id=theatre.user_id)
    user.delete()
    theatre.delete()
    return HttpResponseRedirect('/admin-view-theatre')




@login_required(login_url='adminlogin')
def admin_producer_view(request):
    return render(request,'multiplex/admin_producer.html')

@login_required(login_url='adminlogin')
def admin_approve_producer_view(request):
    producers=models.Producer.objects.all().filter(status=False)
    return render(request,'multiplex/admin_approve_producer.html',{'producers':producers})

@login_required(login_url='adminlogin')
def approve_producer_view(request,pk):
    producer=models.Producer.objects.get(id=pk)
    producer.status=True
    producer.save()
    return HttpResponseRedirect('/admin-approve-producer')

@login_required(login_url='adminlogin')
def delete_producer_view(request,pk):
    producer=models.Producer.objects.get(id=pk)
    user=models.User.objects.get(id=producer.user_id)
    user.delete()
    producer.delete()
    return HttpResponseRedirect('/admin-approve-producer')


@login_required(login_url='adminlogin')
def admin_distributor_view(request):
    return render(request,'multiplex/admin_distributor.html')

@login_required(login_url='adminlogin')
def admin_approve_distributor_view(request):
    distributors=models.Distributor.objects.all().filter(status=False)
    return render(request,'multiplex/admin_approve_distributor.html',{'distributors':distributors})

@login_required(login_url='adminlogin')
def approve_distributor_view(request,pk):
    distributor=models.Distributor.objects.get(id=pk)
    distributor.status=True
    distributor.save()
    return HttpResponseRedirect('/admin-approve-distributor')

@login_required(login_url='adminlogin')
def delete_distributor_view(request,pk):
    distributor=models.Distributor.objects.get(id=pk)
    user=models.User.objects.get(id=distributor.user_id)
    user.delete()
    distributor.delete()
    return HttpResponseRedirect('/admin-approve-distributor')


@login_required(login_url='adminlogin')
def admin_view_distributor_movie_view(request):
    movies=models.TempMovie.objects.all().exclude(distributor__isnull=True)
    return render(request,'multiplex/admin_view_distributor_movie.html',{'movies':movies})


@login_required(login_url='adminlogin')
def admin_theatre_view(request):
    return render(request,'multiplex/admin_theatre.html')

@login_required(login_url='adminlogin')
def admin_add_theatre_view(request):
    userForm=forms.TheatreUserForm()
    theatreForm=forms.TheatreForm()
    mydict={'userForm':userForm,'theatreForm':theatreForm}
    if request.method=='POST':
        userForm=forms.TheatreUserForm(request.POST)
        theatreForm=forms.TheatreForm(request.POST,request.FILES)
        if userForm.is_valid() and theatreForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            theatre=theatreForm.save(commit=False)
            theatre.user=user
            theatre.status=True
            theatre.save()

            my_theatre_group = Group.objects.get_or_create(name='THEATRE')
            my_theatre_group[0].user_set.add(user)
        return HttpResponseRedirect('admin-view-theatre')
    return render(request,'multiplex/admin_add_theatre.html',context=mydict)


@login_required(login_url='adminlogin')
def admin_approve_theatre_view(request):
    theatres=models.Theatre.objects.all().filter(status=False)
    return render(request,'multiplex/admin_approve_theatre.html',{'theatres':theatres})

@login_required(login_url='adminlogin')
def approve_theatre_view(request,pk):
    theatre=models.Theatre.objects.get(id=pk)
    theatre.status=True
    theatre.save()
    return HttpResponseRedirect('/admin-approve-theatre')

@login_required(login_url='adminlogin')
def delete_theatre_view(request,pk):
    theatre=models.Theatre.objects.get(id=pk)
    user=models.User.objects.get(id=theatre.user_id)
    user.delete()
    theatre.delete()
    return HttpResponseRedirect('/admin-approve-theatre')

@login_required(login_url='adminlogin')
def admin_view_theatre_movie_view(request):
    movies=models.TempMovie.objects.all().exclude(theatre__isnull=True)
    return render(request,'multiplex/admin_view_theatre_movie.html',{'movies':movies})


@login_required(login_url='adminlogin')
def admin_feedback_view(request):
    feedback=models.Feedback.objects.all().order_by('-id')
    return render(request,'multiplex/admin_feedback.html',{'feedback':feedback})
#============================================================================================
# ADMIN RELATED views end
#============================================================================================




#============================================================================================
# PRODUCER RELATED views start
#============================================================================================
@login_required(login_url='producerlogin')
@user_passes_test(is_producer)
def producer_dashboard_view(request):
    producer=models.Producer.objects.get(user_id=request.user.id)
    total=models.TempMovie.objects.filter(producer=producer).filter(producer_status='Sold To Distributor').aggregate(Sum('producer_price')),

    dict={
        'totalmovie':models.TempMovie.objects.filter(producer=producer).count(),
        'totalsoldmovie':models.TempMovie.objects.filter(producer=producer).filter(producer_status='Sold To Distributor').count(),
        'totalunsoldmovie':models.TempMovie.objects.filter(producer=producer).exclude(producer_status='Sold To Distributor').count(),
        'totalcollection':total[0]['producer_price__sum']
            }
    return render(request,'multiplex/producer_dashboard.html',context=dict)

@login_required(login_url='producerlogin')
@user_passes_test(is_producer)
def producer_movie_view(request):
    return render(request,'multiplex/producer_movie.html')


@login_required(login_url='producerlogin')
@user_passes_test(is_producer)
def producer_view_movie_view(request):
    producer=models.Producer.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(producer=producer)
    return render(request,'multiplex/producer_view_movie.html',{'movies':movies})

@login_required(login_url='producerlogin')
@user_passes_test(is_producer)
def producer_delete_movie_view(request,pk):
    movie=models.TempMovie.objects.get(id=pk)
    movie.delete()
    return HttpResponseRedirect('/producer-view-movie')

@login_required(login_url='producerlogin')
@user_passes_test(is_producer)
def producer_add_movie_view(request):
    if request.method=='POST':
        movie=models.TempMovie()
        movie.name=request.POST['name']
        movie.producer_price=int(request.POST['price'])
        movie.producer=models.Producer.objects.get(user_id=request.user.id)
        movie.actor=request.POST['actorname']
        movie.director=request.POST['directorname']
        movie.description=request.POST['description']
        movie.release_date=request.POST['release_date']
        movie.out_date=request.POST['out_date']
        movie.poster=request.FILES['poster']
        movie.video=request.POST['video']
        movie.save()

        return HttpResponseRedirect('producer-view-movie')
    return render(request,'multiplex/producer_add_movie.html')

@login_required(login_url='producerlogin')
@user_passes_test(is_producer)
def producer_sell_movie_view(request):
    producer=models.Producer.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(producer=producer).filter(Q(producer_status="Request Not Made") | Q(producer_status="Request Declined"))
    return render(request,'multiplex/producer_sell_movie.html',{'movies':movies})

@login_required(login_url='producerlogin')
@user_passes_test(is_producer)
def producer_sell_movies_view(request,pk):
    producer=models.Producer.objects.get(user_id=request.user.id)
    movie=models.TempMovie.objects.get(id=pk)
    distributorForm=forms.SellToDistributorsForm()
    if request.method=='POST':
        distributorForm=forms.SellToDistributorsForm(request.POST)
        if distributorForm.is_valid():
            movie.distributor=distributorForm.cleaned_data['distributor']
            movie.producer_status='Request Made'
            movie.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/producer-sell-movie')
    return render(request,'multiplex/producer_sell_movies.html',{'distributorForm':distributorForm})

@login_required(login_url='producerlogin')
@user_passes_test(is_producer)
def producer_view_sold_movies_view(request):
    producer=models.Producer.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(producer=producer).filter(producer_status='Sold To Distributor')
    return render(request,'multiplex/producer_view_sold_movies.html',{'movies':movies})

@login_required(login_url='producerlogin')
@user_passes_test(is_producer)
def producer_collection_view(request):
    producer=models.Producer.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(producer=producer).filter(producer_status="Sold To Distributor")
    return render(request,'multiplex/producer_collection.html',{'movies':movies})


@login_required(login_url='producerlogin')
@user_passes_test(is_producer)
def producer_feedback_view(request):
    feedback=forms.FeedbackForm()
    if request.method=='POST':
        feedback=forms.FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()
        else:
            print("form is invalid")
        return render(request,'multiplex/feedback_sent_by_producer.html')
    return render(request,'multiplex/producer_feedback.html',{'feedback':feedback})
#============================================================================================
# PRODUCER RELATED views END
#============================================================================================




#============================================================================================
# DISTRIBUTOR RELATED views start
#============================================================================================
@login_required(login_url='distributorlogin')
@user_passes_test(is_distributor)
def distributor_dashboard_view(request):
    distributor=models.Distributor.objects.get(user_id=request.user.id)
    total=models.TempMovie.objects.filter(distributor=distributor).filter(distributor_status='Sold To Theatre').aggregate(Sum('distributor_price')),
    dict={
        'totalmovie':models.TempMovie.objects.filter(distributor=distributor).filter(producer_status='Sold To Distributor').count(),
        'totalsoldmovie':models.TempMovie.objects.filter(distributor=distributor).filter(distributor_status='Sold To Theatre').count(),
        'totalunsoldmovie':models.TempMovie.objects.filter(distributor=distributor).filter(producer_status='Sold To Distributor').filter(distributor_status='Request Not Made').count(),
        'totalcollection':total[0]['distributor_price__sum']
    }
    return render(request,'multiplex/distributor_dashboard.html',context=dict)

@login_required(login_url='distributorlogin')
@user_passes_test(is_distributor)
def distributor_movie_view(request):
    return render(request,'multiplex/distributor_movie.html')

@login_required(login_url='distributorlogin')
@user_passes_test(is_distributor)
def distributor_view_movie_view(request):
    distributor=models.Distributor.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(distributor=distributor).filter(producer_status='Sold To Distributor')
    return render(request,'multiplex/distributor_view_movie.html',{'movies':movies})

@login_required(login_url='distributorlogin')
@user_passes_test(is_distributor)
def request_from_producer_view(request):
    distributor=models.Distributor.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(distributor=distributor).filter(producer_status='Request Made')
    return render(request,'multiplex/request_from_producer.html',{'movies':movies})

@login_required(login_url='distributorlogin')
@user_passes_test(is_distributor)
def distributor_accept_request_view(request,pk):
    movie=models.TempMovie.objects.get(id=pk)
    movie.producer_status='Sold To Distributor'
    movie.save()
    distributor=models.Distributor.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(distributor=distributor).filter(producer_status='Request Made')
    return render(request,'multiplex/request_from_producer.html',{'movies':movies})

@login_required(login_url='distributorlogin')
@user_passes_test(is_distributor)
def distributor_reject_request_view(request,pk):
    movie=models.TempMovie.objects.get(id=pk)
    movie.producer_status='Request Declined'
    movie.save()
    distributor=models.Distributor.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(distributor=distributor).filter(producer_status='Request Made')
    return render(request,'multiplex/request_from_producer.html',{'movies':movies})

@login_required(login_url='distributorlogin')
@user_passes_test(is_distributor)
def distributor_sell_movie_view(request):
    distributor=models.Distributor.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(distributor=distributor).filter(producer_status='Sold To Distributor').exclude(distributor_status='Sold To Theatre')
    return render(request,'multiplex/distributor_sell_movie.html',{'movies':movies})

@login_required(login_url='distributorlogin')
@user_passes_test(is_distributor)
def distributor_sell_movies_view(request,pk):
    distributor=models.Distributor.objects.get(user_id=request.user.id)
    movie=models.TempMovie.objects.get(id=pk)
    theatreForm=forms.SellToTheatreForm()
    if request.method=='POST':
        theatreForm=forms.SellToTheatreForm(request.POST)
        if theatreForm.is_valid():
            movie.theatre=theatreForm.cleaned_data['theatre']
            movie.distributor_price=theatreForm.cleaned_data['price']
            movie.distributor_status='Request Made'
            movie.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/distributor-sell-movie')
    return render(request,'multiplex/distributor_sell_movies.html',{'theatreForm':theatreForm})

@login_required(login_url='distributorlogin')
@user_passes_test(is_distributor)
def distributor_view_sold_movies_view(request):
    distributor=models.Distributor.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(distributor=distributor).filter(distributor_status='Sold To Theatre')
    return render(request,'multiplex/distributor_view_sold_movies.html',{'movies':movies})

@login_required(login_url='distributorlogin')
@user_passes_test(is_distributor)
def distributor_collection_view(request):
    distributor=models.Distributor.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(distributor=distributor).filter(distributor_status='Sold To Theatre')
    return render(request,'multiplex/distributor_collection.html',{'movies':movies})

@login_required(login_url='distributorlogin')
@user_passes_test(is_distributor)
def distributor_feedback_view(request):
    feedback=forms.FeedbackForm()
    if request.method=='POST':
        feedback=forms.FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()
        else:
            print("form is invalid")
        return render(request,'multiplex/feedback_sent_by_distributor.html')
    return render(request,'multiplex/distributor_feedback.html',{'feedback':feedback})
#============================================================================================
# DISTRIBUTOR RELATED views END
#============================================================================================






#============================================================================================
# Theatre RELATED views start
#============================================================================================
@login_required(login_url='theatrelogin')
@user_passes_test(is_theatre)
def theatre_dashboard_view(request):
    theatre=models.Theatre.objects.get(user_id=request.user.id)

    moviess=models.Movie.objects.filter(theatre=theatre)
    totalcollection=0
    for movie in moviess:
        bookings=models.Booking.objects.filter(movie=movie)
        for booking in bookings:
            totalcollection=totalcollection+booking.cost

    movies=models.TempMovie.objects.filter(theatre=theatre).filter(distributor_status='Sold To Theatre')
    dict={
    'totalmovie':models.TempMovie.objects.filter(theatre=theatre).filter(distributor_status='Sold To Theatre').count(),
    'totalreleasedmovie':models.TempMovie.objects.filter(theatre=theatre).filter(theatre_status='Movie Released').count(),
    'totalrequest':models.TempMovie.objects.filter(theatre=theatre).filter(distributor_status='Request Made').count(),
    'totalcollection':totalcollection,
    }
    return render(request,'multiplex/theatre_dashboard.html',context=dict)


@login_required(login_url='theatrelogin')
@user_passes_test(is_theatre)
def theatre_movie_view(request):
    return render(request,'multiplex/theatre_movie.html')

@login_required(login_url='theatrelogin')
@user_passes_test(is_theatre)
def theatre_view_movie_view(request):
    theatre=models.Theatre.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(theatre=theatre).filter(distributor_status='Sold To Theatre')
    return render(request,'multiplex/theatre_view_movie.html',{'movies':movies})

@login_required(login_url='theatrelogin')
@user_passes_test(is_theatre)
def request_from_distributor_view(request):
    theatre=models.Theatre.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(theatre=theatre).filter(distributor_status='Request Made')
    return render(request,'multiplex/request_from_distributor.html',{'movies':movies})

@login_required(login_url='theatrelogin')
@user_passes_test(is_theatre)
def theatre_accept_request_view(request,pk):
    movie=models.TempMovie.objects.get(id=pk)
    movie.distributor_status='Sold To Theatre'
    movie.save()
    theatre=models.Theatre.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(theatre=theatre).filter(distributor_status='Request Made')
    return render(request,'multiplex/request_from_distributor.html',{'movies':movies})

@login_required(login_url='theatrelogin')
@user_passes_test(is_theatre)
def theatre_reject_request_view(request,pk):
    movie=models.TempMovie.objects.get(id=pk)
    movie.distributor_status='Request Declined'
    movie.save()
    theatre=models.Theatre.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(theatre=theatre).filter(distributor_status='Request Made')
    return render(request,'multiplex/request_from_distributor.html',{'movies':movies})

@login_required(login_url='theatrelogin')
@user_passes_test(is_theatre)
def theatre_release_movie_view(request):
    theatre=models.Theatre.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(theatre=theatre).filter(distributor_status='Sold To Theatre').filter(theatre_status='Movie Not Released')
    return render(request,'multiplex/theatre_release_movie.html',{'movies':movies})

@login_required(login_url='theatrelogin')
@user_passes_test(is_theatre)
def theatre_release_movies_view(request,pk):
    theatre=models.Theatre.objects.get(user_id=request.user.id)
    movie=models.TempMovie.objects.get(id=pk)
    movie.theatre_status='Movie Released'
    movie.save()

    original_movie=models.Movie()
    original_movie.name=movie.name
    original_movie.actor=movie.actor
    original_movie.director=movie.director
    original_movie.description=movie.description
    original_movie.release_date=movie.release_date
    original_movie.out_date=movie.out_date
    original_movie.poster=movie.poster
    original_movie.video=movie.video
    original_movie.theatre=theatre
    original_movie.save()


    #for making seat available between release date and out_date
    start_date = movie.release_date
    #start_date=date(int(start_date[0:4]),int(start_date[5:7]),int(start_date[8:10]))
    end_date = movie.out_date
    #end_date=date(int(end_date[0:4]),int(end_date[5:7]),int(end_date[8:10]))
    delta = timedelta(days=1)
    moviex=models.Movie.objects.get(id=original_movie.id)
    while start_date <= end_date:
        seat=models.Seat(movie=moviex,date=start_date)
        seat.save()
        start_date += delta

    return HttpResponseRedirect('/theatre-release-movie')

@login_required(login_url='theatrelogin')
@user_passes_test(is_theatre)
def theatre_view_released_movie_view(request):
    theatre=models.Theatre.objects.get(user_id=request.user.id)
    movies=models.TempMovie.objects.filter(theatre=theatre).filter(distributor_status='Sold To Theatre').filter(theatre_status='Movie Released')
    return render(request,'multiplex/theatre_view_released_movie.html',{'movies':movies})

@login_required(login_url='theatrelogin')
@user_passes_test(is_theatre)
def theatre_collection_view(request):
    theatre=models.Theatre.objects.get(user_id=request.user.id)
    movies=models.Movie.objects.filter(theatre=theatre)
    movies_collection=[]
    movie_names=[]
    for movie in movies:
        cost=0
        bookings=models.Booking.objects.filter(movie=movie)
        for booking in bookings:
            cost=cost+booking.cost
        movies_collection.append(cost)
        movie_names.append(movie)
    data=zip(movie_names,movies_collection)
    return render(request,'multiplex/theatre_collection_view.html',{'data':data})


@login_required(login_url='theatrelogin')
@user_passes_test(is_theatre)
def theatre_feedback_view(request):
    feedback=forms.FeedbackForm()
    if request.method=='POST':
        feedback=forms.FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()
        else:
            print("form is invalid")
        return render(request,'multiplex/feedback_sent_by_theatre.html')
    return render(request,'multiplex/theatre_feedback.html',{'feedback':feedback})
#============================================================================================
# Theatre RELATED views END
#============================================================================================






#============================================================================================
# CUSTOMER RELATED views start
#============================================================================================
@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_dashboard_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    bookings=models.Booking.objects.filter(customer=customer).order_by('-id')
    dict={}
    for booking in bookings:
        dict={
        'customer':customer,
        'movieName':booking.movie,
        'seatNumber':booking.seatNumber,
        'cost':booking.cost,
        'movieDate':booking.date,
        }
        break
    return render(request,'multiplex/customer_dashboard.html',context=dict)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_home_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    movies=models.Movie.objects.all()
    dict={
    'customer':customer,
    'movies':movies,
    }
    return render(request,'multiplex/customer_home.html',context=dict)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def view_movie_details_view(request,pk):
    movie=models.Movie.objects.get(id=pk)
    dict={
    'movie':movie,
    'customer':models.Customer.objects.get(user_id=request.user.id)
    }
    return render(request,'multiplex/view_movie_details.html',context=dict)



@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_profile_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    return render(request,'multiplex/customer_profile.html',{'customer':customer})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def edit_customer_profile_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    user=models.User.objects.get(id=customer.user_id)
    userForm=forms.CustomerUserForm(instance=user)
    customerForm=forms.CustomerForm(request.FILES,instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm,'customer':customer}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST,instance=user)
        customerForm=forms.CustomerForm(request.POST,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return HttpResponseRedirect('customer-profile')
    return render(request,'multiplex/edit_customer_profile.html',context=mydict)



@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def book_now_view(request,pk):
    movie=models.Movie.objects.get(id=pk)
    release_date=movie.release_date
    out_date=movie.out_date
    customer=models.Customer.objects.get(user_id=request.user.id)
    dict={
    'release_date':str(release_date),
    'out_date':str(out_date),
    'movie':movie,
    'customer':customer,
    }
    if request.method=='POST':
        booking_date=request.POST['booking_date']
        #pk is movie id and booking id...... we will fetch seat availability and show to the user
        seats=models.Seat.objects.get(movie=movie,date=booking_date)
        request.session['movie_id']=movie.id
        request.session['seat_id']=seats.id
        return HttpResponseRedirect('/choose-seat')

    return render(request,'multiplex/ask_booking_date.html',context=dict)

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def choose_seat_view(request):
    movie=models.Movie.objects.get(id=request.session['movie_id'])
    seats=models.Seat.objects.get(id=request.session['seat_id'])

    dict={
    'movie':movie,
    'seats':seats,
    }
    response= render(request,'multiplex/choose_seat.html',context=dict)
    response.set_cookie('movie_id',request.session['movie_id'])
    response.set_cookie('seat_id',request.session['seat_id'])
    return response

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def proceed_to_pay_view(request):
    total=int(request.COOKIES['allNumberVals'])*100
    totalSeat=int(request.COOKIES['allNumberVals'])
    return render(request,'multiplex/payment.html',{'total':total,'totalSeat':totalSeat})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def payment_success_view(request):
    movie=models.Movie.objects.get(id=request.COOKIES['movie_id'])
    seats=models.Seat.objects.get(id=request.COOKIES['seat_id'])
    allNameVals=request.COOKIES['allNameVals']
    allNumberVals=request.COOKIES['allNumberVals']
    allSeatsVals=request.COOKIES['allSeatsVals']
    total=int(request.COOKIES['allNumberVals'])*100

    #make seat unavailable for other
    seat=allSeatsVals.split(',')
    for x in seat:
        if x=='A1':
            seats.A1=False
        elif x=='A2':
            seats.A2=False
        elif x=='A3':
            seats.A3=False
        elif x=='A4':
            seats.A4=False
        elif x=='A5':
            seats.A5=False
        elif x=='A6':
            seats.A6=False
        elif x=='A7':
            seats.A7=False
        elif x=='A8':
            seats.A8=False
        elif x=='A9':
            seats.A9=False
        elif x=='A10':
            seats.A10=False
        elif x=='A11':
            seats.A11=False
        elif x=='A12':
            seats.A12=False
        elif x=='B1':
            seats.B1=False
        elif x=='B2':
            seats.B2=False
        elif x=='B3':
            seats.B3=False
        elif x=='B4':
            seats.B4=False
        elif x=='B5':
            seats.B5=False
        elif x=='B6':
            seats.B6=False
        elif x=='B7':
            seats.B7=False
        elif x=='B8':
            seats.B8=False
        elif x=='B9':
            seats.B9=False
        elif x=='B10':
            seats.B10=False
        elif x=='B11':
            seats.B11=False
        elif x=='B12':
            seats.B12=False
        elif x=='C1':
            seats.C2=False
        elif x=='C3':
            seats.C3=False
        elif x=='C4':
            seats.C4=False
        elif x=='C5':
            seats.C6=False
        elif x=='C7':
            seats.C8=False
        elif x=='C9':
            seats.C9=False
        elif x=='C10':
            seats.C10=False
        elif x=='C11':
            seats.C11=False
        elif x=='C12':
            seats.C12=False
        elif x=='D1':
            seats.D1=False
        elif x=='D2':
            seats.D2=False
        elif x=='D3':
            seats.D3=False
        elif x=='D4':
            seats.D4=False
        elif x=='D5':
            seats.D5=False
        elif x=='D6':
            seats.D6=False
        elif x=='D7':
            seats.D7=False
        elif x=='D8':
            seats.D8=False
        elif x=='D9':
            seats.D9=False
        elif x=='D10':
            seats.D10=False
        elif x=='D11':
            seats.D11=False
        elif x=='D12':
            seats.D12=False
        elif x=='E1':
            seats.E1=False
        elif x=='E2':
            seats.E2=False
        elif x=='E3':
            seats.E3=False
        elif x=='E4':
            seats.E4=False
        elif x=='E5':
            seats.E5=False
        elif x=='E6':
            seats.E6=False
        elif x=='E7':
            seats.E7=False
        elif x=='E8':
            seats.E8=False
        elif x=='E9':
            seats.E9=False
        elif x=='E10':
            seats.E10=False
        elif x=='E11':
            seats.E11=False
        elif x=='E12':
            seats.E12=False
        elif x=='F1':
            seats.F1=False
        elif x=='F2':
            seats.F2=False
        elif x=='F3':
            seats.F3=False
        elif x=='F4':
            seats.F4=False
        elif x=='F5':
            seats.F5=False
        elif x=='F6':
            seats.F6=False
        elif x=='F7':
            seats.F7=False
        elif x=='F8':
            seats.F8=False
        elif x=='F9':
            seats.F9=False
        elif x=='F10':
            seats.F10=False
        elif x=='F11':
            seats.F11=False
        elif x=='F12':
            seats.F12=False
        elif x=='G1':
            seats.G1=False
        elif x=='G2':
            seats.G2=False
        elif x=='G3':
            seats.G3=False
        elif x=='G4':
            seats.G4=False
        elif x=='G5':
            seats.G5=False
        elif x=='G6':
            seats.G6=False
        elif x=='G7':
            seats.G7=False
        elif x=='G8':
            seats.G8=False
        elif x=='G9':
            seats.G9=False
        elif x=='G10':
            seats.G10=False
        elif x=='G11':
            seats.G11=False
        elif x=='G12':
            seats.G12=False
        elif x=='H1':
            seats.H1=False
        elif x=='H2':
            seats.H2=False
        elif x=='H3':
            seats.H3=False
        elif x=='H4':
            seats.H4=False
        elif x=='H5':
            seats.H5=False
        elif x=='H6':
            seats.H6=False
        elif x=='H7':
            seats.H7=False
        elif x=='H8':
            seats.H8=False
        elif x=='H9':
            seats.H9=False
        elif x=='H10':
            seats.H10=False
        elif x=='H11':
            seats.H11=False
        elif x=='H12':
            seats.H12=False
        elif x=='I1':
            seats.I1=False
        elif x=='I2':
            seats.I2=False
        elif x=='I3':
            seats.I3=False
        elif x=='I4':
            seats.I4=False
        elif x=='I5':
            seats.I5=False
        elif x=='I6':
            seats.I6=False
        elif x=='I7':
            seats.I7=False
        elif x=='I8':
            seats.I8=False
        elif x=='I9':
            seats.I9=False
        elif x=='I10':
            seats.I10=False
        elif x=='I11':
            seats.I11=False
        elif x=='I12':
            seats.I12=False
        elif x=='J1':
            seats.J1=False
        elif x=='J2':
            seats.J2=False
        elif x=='J3':
            seats.J3=False
        elif x=='J4':
            seats.J4=False
        elif x=='J5':
            seats.J5=False
        elif x=='J6':
            seats.J6=False
        elif x=='J7':
            seats.J7=False
        elif x=='J8':
            seats.J8=False
        elif x=='J9':
            seats.J9=False
        elif x=='J10':
            seats.J10=False
        elif x=='J11':
            seats.J11=False
        elif x=='J12':
            seats.J12=False

    seats.save()


    #create booking object
    customer=models.Customer.objects.get(user_id=request.user.id)
    booking=models.Booking()
    booking.customer=customer
    booking.movie=movie
    booking.cost=total
    booking.totalSeat=int(request.COOKIES['allNumberVals'])
    booking.seatNumber=allSeatsVals
    booking.date=seats.date
    booking.watchers=allNameVals
    booking.save()

    return render(request,'multiplex/movie_booked.html',{'customer':customer})


import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def download_ticket_view(request):

    mydict={
    'movie':models.Movie.objects.get(id=request.COOKIES['movie_id']),
    'customer':models.Customer.objects.get(user_id=request.user.id),
    'seats':models.Seat.objects.get(id=request.COOKIES['seat_id']),
    'allNameVals':request.COOKIES['allNameVals'],
    'allNumberVals':request.COOKIES['allNumberVals'],
    'allSeatsVals':request.COOKIES['allSeatsVals'],
    'total':int(request.COOKIES['allNumberVals'])*100,
    }
    return render_to_pdf('multiplex/download_ticket.html',mydict)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_feedback_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    feedback=forms.FeedbackForm()
    if request.method=='POST':
        feedback=forms.FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()
        else:
            print("form is invalid")
        return render(request,'multiplex/feedback_sent_by_customer.html',{'customer':customer})
    return render(request,'multiplex/customer_feedback.html',{'feedback':feedback,'customer':customer})


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_ticket_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    bookings=models.Booking.objects.filter(customer=customer).order_by('-id')
    dict={
    'customer':customer,
    'bookings':bookings,
    }
    return render(request,'multiplex/customer_ticket.html',context=dict)


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def download_tickets_view(request,pk):
    booking=models.Booking.objects.get(id=pk)
    customer=models.Customer.objects.get(user_id=request.user.id)
    mydict={
    'movie':models.Movie.objects.get(id=booking.movie_id),
    'customer':models.Customer.objects.get(user_id=request.user.id),
    'booking':booking,
    }
    return render_to_pdf('multiplex/download_tickets.html',mydict)


#============================================================================================
# OTHER views start
#============================================================================================
def view_movie_detailss_view(request,pk):
    movie=models.Movie.objects.get(id=pk)
    dict={
    'movie':movie,
    }
    return render(request,'multiplex/view_movie_detailss.html',context=dict)

# for aboutus and contact
def aboutus_view(request):
    return render(request,'multiplex/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'multiplex/contactussuccess.html')
    return render(request, 'multiplex/contactus.html', {'form':sub})
