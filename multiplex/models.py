from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,default='images/user.jpg',blank=True)
    address = models.CharField(max_length=40,null=True)
    mobile = models.CharField(max_length=20,null=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name


class Producer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/ProducerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    #status for account is approved or not by admin
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name

class Distributor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DistributorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    #status for account is approved or not by admin
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name

class Theatre(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/TheatreProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    #status for account is approved or not by admin
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name



class Movie(models.Model):
    name=models.CharField(max_length=50,null=True)
    actor=models.CharField(max_length=50,null=True)
    director=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=500,null=True)
    poster=models.ImageField(upload_to='movie_pic/movie_poster/',null=True,blank=True)
    video=models.CharField(max_length=200,null=True)
    release_date=models.DateField()
    out_date=models.DateField()
    theatre=models.ForeignKey('Theatre',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

#movies that will be added by producer then sold to distributor then sold to theatres
#if theatres accept it then Movie object will be created with TempMovie
class TempMovie(models.Model):
    name=models.CharField(max_length=50,null=True)
    actor=models.CharField(max_length=50,null=True)
    director=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=100,null=True)
    poster=models.ImageField(upload_to='temp_movie_pic/movie_poster/',null=True,blank=True)
    video=models.CharField(max_length=200,null=True)
    release_date=models.DateField()
    out_date=models.DateField()

    producer=models.ForeignKey('Producer',on_delete=models.CASCADE)
    producer_price=models.PositiveIntegerField()
    #status for buying and selling
    cat=(('Request Not Made','Request Not Made'),('Sold To Distributor','Sold To Distributor'),('Request Made','Request Made'),('Request Declined','Request Declined'))
    producer_status=models.CharField(max_length=80,choices=cat,default='Request Not Made')

    distributor=models.ForeignKey('Distributor',on_delete=models.CASCADE,null=True)
    distributor_price=models.PositiveIntegerField(null=True)
    #status for buying and selling
    cat1=(('Request Not Made','Request Not Made'),('Sold To Theatre','Sold To Theatre'),('Request Made','Request Made'),('Request Declined','Request Declined'))
    distributor_status=models.CharField(max_length=50,choices=cat1,default='Request Not Made')
    theatre=models.ForeignKey('Theatre',on_delete=models.CASCADE,null=True)
    cat2=(('Movie Released','Movie Released'),('Movie Not Released','Movie Not Released'))
    theatre_status=models.CharField(max_length=80,choices=cat2,default='Movie Not Released')
    def __str__(self):
        return self.name


class Feedback(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=40)
    message=models.CharField(max_length=500)

class Booking(models.Model):
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,null=True)
    movie=models.ForeignKey('Movie',on_delete=models.CASCADE,null=True)
    date=models.DateField()
    seatNumber=models.CharField(max_length=500)
    totalSeat=models.PositiveIntegerField()
    cost=models.PositiveIntegerField()
    watchers=models.CharField(max_length=500,null=True)
    bookingDate=models.DateField(auto_now=True)
    def __str__(self):
        return self.customer

class Seat(models.Model):
    movie=models.ForeignKey('Movie', on_delete=models.CASCADE,null=True)
    date=models.DateField()

    #for seat available or not true=available and false means not available, default available
    # whenever movie will be added seat will be also created
    A1=models.BooleanField(default=True)
    A2=models.BooleanField(default=True)
    A3=models.BooleanField(default=True)
    A4=models.BooleanField(default=True)
    A5=models.BooleanField(default=True)
    A6=models.BooleanField(default=True)
    A7=models.BooleanField(default=True)
    A8=models.BooleanField(default=True)
    A9=models.BooleanField(default=True)
    A10=models.BooleanField(default=True)
    A11=models.BooleanField(default=True)
    A12=models.BooleanField(default=True)
    B1=models.BooleanField(default=True)
    B2=models.BooleanField(default=True)
    B3=models.BooleanField(default=True)
    B4=models.BooleanField(default=True)
    B5=models.BooleanField(default=True)
    B6=models.BooleanField(default=True)
    B7=models.BooleanField(default=True)
    B8=models.BooleanField(default=True)
    B9=models.BooleanField(default=True)
    B10=models.BooleanField(default=True)
    B11=models.BooleanField(default=True)
    B12=models.BooleanField(default=True)
    C1=models.BooleanField(default=True)
    C2=models.BooleanField(default=True)
    C3=models.BooleanField(default=True)
    C4=models.BooleanField(default=True)
    C5=models.BooleanField(default=True)
    C6=models.BooleanField(default=True)
    C7=models.BooleanField(default=True)
    C8=models.BooleanField(default=True)
    C9=models.BooleanField(default=True)
    C10=models.BooleanField(default=True)
    C11=models.BooleanField(default=True)
    C12=models.BooleanField(default=True)
    D1=models.BooleanField(default=True)
    D2=models.BooleanField(default=True)
    D3=models.BooleanField(default=True)
    D4=models.BooleanField(default=True)
    D5=models.BooleanField(default=True)
    D6=models.BooleanField(default=True)
    D7=models.BooleanField(default=True)
    D8=models.BooleanField(default=True)
    D9=models.BooleanField(default=True)
    D10=models.BooleanField(default=True)
    D11=models.BooleanField(default=True)
    D12=models.BooleanField(default=True)
    E1=models.BooleanField(default=True)
    E2=models.BooleanField(default=True)
    E3=models.BooleanField(default=True)
    E4=models.BooleanField(default=True)
    E5=models.BooleanField(default=True)
    E6=models.BooleanField(default=True)
    E7=models.BooleanField(default=True)
    E8=models.BooleanField(default=True)
    E9=models.BooleanField(default=True)
    E10=models.BooleanField(default=True)
    E11=models.BooleanField(default=True)
    E12=models.BooleanField(default=True)
    F1=models.BooleanField(default=True)
    F2=models.BooleanField(default=True)
    F3=models.BooleanField(default=True)
    F4=models.BooleanField(default=True)
    F5=models.BooleanField(default=True)
    F6=models.BooleanField(default=True)
    F7=models.BooleanField(default=True)
    F8=models.BooleanField(default=True)
    F9=models.BooleanField(default=True)
    F10=models.BooleanField(default=True)
    F11=models.BooleanField(default=True)
    F12=models.BooleanField(default=True)
    G1=models.BooleanField(default=True)
    G2=models.BooleanField(default=True)
    G3=models.BooleanField(default=True)
    G4=models.BooleanField(default=True)
    G5=models.BooleanField(default=True)
    G6=models.BooleanField(default=True)
    G7=models.BooleanField(default=True)
    G8=models.BooleanField(default=True)
    G9=models.BooleanField(default=True)
    G10=models.BooleanField(default=True)
    G11=models.BooleanField(default=True)
    G12=models.BooleanField(default=True)
    H1=models.BooleanField(default=True)
    H2=models.BooleanField(default=True)
    H3=models.BooleanField(default=True)
    H4=models.BooleanField(default=True)
    H5=models.BooleanField(default=True)
    H6=models.BooleanField(default=True)
    H7=models.BooleanField(default=True)
    H8=models.BooleanField(default=True)
    H9=models.BooleanField(default=True)
    H10=models.BooleanField(default=True)
    H11=models.BooleanField(default=True)
    H12=models.BooleanField(default=True)
    I1=models.BooleanField(default=True)
    I2=models.BooleanField(default=True)
    I3=models.BooleanField(default=True)
    I4=models.BooleanField(default=True)
    I5=models.BooleanField(default=True)
    I6=models.BooleanField(default=True)
    I7=models.BooleanField(default=True)
    I8=models.BooleanField(default=True)
    I9=models.BooleanField(default=True)
    I10=models.BooleanField(default=True)
    I11=models.BooleanField(default=True)
    I12=models.BooleanField(default=True)
    J1=models.BooleanField(default=True)
    J2=models.BooleanField(default=True)
    J3=models.BooleanField(default=True)
    J4=models.BooleanField(default=True)
    J5=models.BooleanField(default=True)
    J6=models.BooleanField(default=True)
    J7=models.BooleanField(default=True)
    J8=models.BooleanField(default=True)
    J9=models.BooleanField(default=True)
    J10=models.BooleanField(default=True)
    J11=models.BooleanField(default=True)
    J12=models.BooleanField(default=True)
