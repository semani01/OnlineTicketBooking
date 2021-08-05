# MOVIE TICKET BOOKING
![developer](https://img.shields.io/badge/Developed%20By%20%3A-Sumit%20Kumar-red)
---
## SCREENSHOTS
### Home Page
![home snap](https://github.com/sumitkumar1503/movieticketbooking/blob/master/static/screenshot/home.png?raw=true)
### Download Ticket
![ticket snap](https://github.com/sumitkumar1503/movieticketbooking/blob/master/static/screenshot/ticket.png?raw=true)
### Admin View Movie
![admin snap](https://github.com/sumitkumar1503/movieticketbooking/blob/master/static/screenshot/admin.png?raw=true)
### Seat Choose
![seat snap](https://github.com/sumitkumar1503/movieticketbooking/blob/master/static/screenshot/seat_choose.png?raw=true)
### Theatre Collection
![theatre snap](https://github.com/sumitkumar1503/movieticketbooking/blob/master/static/screenshot/theatre.png?raw=true)
---
## FUNCTIONS
### BASIC FLOW
- Customer will login to system, book ticket, Download ticket...
- Producer will add their film, then he/she will request DISTRIBUTOR to buy their film, If DISTRIBUTOR agree with producer film price, then DISTRIBUTOR will accept request from PRODUCER.
- Now Distributor will further sell those film (bought from producer) to THEATRE OWNER with their own price, It will send request to THEATRE OWNER, IF theatre owner agree with DISTRIBUTOR price then theatre will buy those film and release to theatre.
- Customer can book only those movie that is released by THEATRE or added by ADMIN, not by PRODUCER or DISTRIBUTOR
- There is 5 roles

---

### CUSTOMER
- Customer can view movie details (trailer, actor, director, etc.) on Home Page without log in into system.
- FOR BOOKING TICKET
- customer have to login, It will ask enter booking date (customer can select only date between release date and out date)
- After that, customer have to choose seats, customer can choose seat after entering details like name (who will watch movie) and total seat and click on start selecting.
- Now customer can choose seats, customer can not choose more or less than the seat number they have provided in above steps.
- Customer are not allowed to choose seat that are already booked by another customer on the same date/movie.
- After selecting seat, click on confirm selection, It will show seat numbers, And PAYMENT BUTTON will appear
- After clicking on Pay, there is payment form, where customers are asked to fill card details (DO NOT ENTER CARD DETAILS)(SYSTEM DO NOT SAVE DETAILS)
- Simply click on pay, payment will be successful, Now customers ticket is booked.

- Customer can view their booked movies details.
- Customer can download movies tickets
- Customer can view their profile and edit it.
- Customer can send feedback to admin

---

### PRODUCER
- First producer will create account, after account approval from admin, producer can login.
- Producer can add their film, there is release date and out date, out date means when this film gonna exit from theatre, means CUSTOMER will not be allowed to book ticket after out date.
- NOTE : out date must be greater than release date.
- Producer have to provide trailer video (YouTube link) while adding film, so that customer can watch it.
- Producer can view/delete their movie.
- Producer can sell their movie to distributors, but there must be distributors account registered, so that producer can choose distributors.
- Producer can view sold movies (request accepted by distributor).
- Producer can view sold movies Collection.
- Producer can send feedback to Admin.

---

### DISTRIBUTOR
- First distributor will create account, after account approval from admin, distributor can login.
- Distributor can view request of movies sent by producer, distributor can accept the request if distributor agree on producer price or reject request if not agree on price.
- If distributor accepted the request, it means that movie is sold to distributor, and producer got the price.
- Distributor can further sell movies to Theatre with their own price. (For that there must be theatre accounts registered)
- If theatre accepted distributor request or agree on distributor price, It means distributor sold that movie to theatre.
- Distributor can see how many movies they have sold to theatre, bought from producer.
- Distributor can see Collection, how much profit earned.
- Distributor can send feedback to admin.

---

### THEATRE
- First theatre will create account, after account approval from admin, theatre can login.
- Theatre can view request of movies sent by distributor, theatre can accept the request if theatre agree on distributor price or reject request if not agree on price.
- If theatre accepted the request, it means that movie is sold to theatre, and distributor got the price.
- Now theatre can release movie (that are bought from distributor).
- Whenever theatre click on release movie, IT WILL BE AVAILABLE FOR CUSTOMERS TO BOOK TICKETS.

- Theatre can view collection of each released movie. Theatre Collection is based on customer bookings,
 If theatre released one movie named *BAHUBALI*, and total ticket booked for *BAHUBALI* is 20,
 then theatre collection for film *BAHUBALI* will be 20*100 = 2000 (ONE TICKET COST 100, ITS FIXED),
 Its real time collection, means if another customer booked one more ticket, then collection will be updated as 2100.

- Theatre can view how many movies he/she bought from distributor and released.
- Theatre can see total released movie collection on dashboard.
- Theatre can send feedback to admin.

---

### Admin
- After login into system, on dashboard admin can how many customer, producer, distributor, theatre is registered.
- Admin can view/delete/add movies.
- Admin can view released and not released movie (not released means, movie that is added by producer is under buying selling process).
- Admin can view/delete/add customers.
- Admin can view customers booking and can delete that bookings.
- Admin can view/add/delete PRODUCER, DISTRIBUTOR, THEATRE.
- Admin can approve PRODUCER, DISTRIBUTOR, THEATRE accounts (NO APPROVAL REQUIRED FOR CUSTOMER ACCOUNT).
- Admin can view PRODUCER, DISTRIBUTOR, THEATRE films.
- Admin can view feedbacks sent by customer, producer, distributor, theatre.

---

### Other Features
- User can change theme of website (day and night)
- If Movie deleted by admin then all bookings are cancelled.

---

## Drawbacks/LoopHoles
- On seat choose page, already booked seat by another customer is showing empty, However customer can not choose that seat. ITS DISABLED :)

---

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
pip install django==3.0.5
pip install django-widget-tweaks
pip install xhtml2pdf

```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
- Give username, email, password and your admin account will be created.
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```

## CHANGES REQUIRED FOR CONTACT US PAGE
- In settins.py file, You have to give your email and password
```
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your email password'
EMAIL_RECEIVING_USER = 'youremail@gmail.com'
```
- Login to gmail through host email id in your browser and open following link and turn it ON
```
https://myaccount.google.com/lesssecureapps
```

## Disclaimer
This project is developed for demo purpose and it's not supposed to be used in real application.

## Feedback
Any suggestion and feedback is welcome. You can message me on facebook
- [Contact on Facebook](https://fb.com/sumit.luv)
- [Subscribe my Channel LazyCoder On Youtube](https://youtube.com/lazycoders)
