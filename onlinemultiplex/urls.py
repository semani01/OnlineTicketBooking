from django.contrib import admin
from django.urls import path
from multiplex import views
from movieapi.views import occupy,vacate,get_info
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('occupy',occupy),
    path('vacate',vacate),
    path('get-info',get_info),



    path('adminclick', views.adminclick_view),
    path('customerclick', views.customerclick_view),
    path('producerclick', views.producerclick_view),
    path('distributorclick', views.distributorclick_view),
    path('theatreclick', views.theatreclick_view),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),

    path('customersignup', views.customer_signup_view,name='customersignup'),
    path('customerlogin', LoginView.as_view(template_name='multiplex/customerlogin.html'),name='customerlogin'),

    path('producersignup', views.producer_signup_view,name='producersignup'),
    path('producerlogin', LoginView.as_view(template_name='multiplex/producerlogin.html'),name='producerlogin'),
    path('producer-dashboard', views.producer_dashboard_view,name='producer-dashboard'),
    path('producer-feedback', views.producer_feedback_view,name='producer-feedback'),
    path('producer-movie', views.producer_movie_view,name='producer-movie'),
    path('producer-add-movie', views.producer_add_movie_view,name='producer-add-movie'),
    path('producer-view-movie', views.producer_view_movie_view,name='producer-view-movie'),
    path('producer-delete-movie/<int:pk>', views.producer_delete_movie_view,name='producer-delete-movie'),
    path('producer-sell-movie', views.producer_sell_movie_view,name='producer-sell-movie'),
    path('producer-sell-movies/<int:pk>', views.producer_sell_movies_view,name='producer-sell-movies'),
    path('producer-view-sold-movies', views.producer_view_sold_movies_view,name='producer-view-sold-movies'),
    path('producer-collection', views.producer_collection_view,name='producer-collection'),



    path('distributorsignup', views.distributor_signup_view,name='distributorsignup'),
    path('distributorlogin', LoginView.as_view(template_name='multiplex/distributorlogin.html'),name='distributorlogin'),
    path('distributor-dashboard', views.distributor_dashboard_view,name='distributor-dashboard'),
    path('distributor-feedback', views.distributor_feedback_view,name='distributor-feedback'),
    path('distributor-movie', views.distributor_movie_view,name='distributor-movie'),
    path('distributor-view-movie', views.distributor_view_movie_view,name='distributor-view-movie'),
    path('request-from-producer', views.request_from_producer_view,name='request-from-producer'),
    path('distributor-accept-request/<int:pk>', views.distributor_accept_request_view,name='distributor-accept-request'),
    path('distributor-reject-request/<int:pk>', views.distributor_reject_request_view,name='distributor-reject-request'),
    path('distributor-sell-movie', views.distributor_sell_movie_view,name='distributor-sell-movie'),
    path('distributor-sell-movies/<int:pk>', views.distributor_sell_movies_view,name='distributor-sell-movies'),
    path('distributor-view-sold-movies', views.distributor_view_sold_movies_view,name='distributor-view-sold-movies'),
    path('distributor-collection', views.distributor_collection_view,name='distributor-collection'),


    path('theatresignup', views.theatre_signup_view,name='theatresignup'),
    path('theatrelogin', LoginView.as_view(template_name='multiplex/theatrlogin.html'),name='theatrelogin'),
    path('theatre-dashboard', views.theatre_dashboard_view,name='theatre-dashboard'),
    path('theatre-feedback', views.theatre_feedback_view,name='theatre-feedback'),
    path('theatre-movie', views.theatre_movie_view,name='theatre-movie'),
    path('theatre-view-movie', views.theatre_view_movie_view,name='theatre-view-movie'),
    path('request-from-distributor', views.request_from_distributor_view,name='request-from-distributor'),
    path('theatre-accept-request/<int:pk>', views.theatre_accept_request_view,name='theatre-accept-request'),
    path('theatre-reject-request/<int:pk>', views.theatre_reject_request_view,name='theatre-reject-request'),
    path('theatre-release-movie', views.theatre_release_movie_view,name='theatre-release-movie'),
    path('theatre-release-movies/<int:pk>', views.theatre_release_movies_view,name='theatre-release-movies'),
    path('theatre-view-released-movie', views.theatre_view_released_movie_view,name='theatre-view-released-movie'),
    path('theatre-collection', views.theatre_collection_view,name='theatre-collection'),







    path('admin-customer', views.admin_customer_view,name='admin-customer'),
    path('admin-view-customer', views.admin_view_customer_view,name='admin-view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('admin-add-customer', views.admin_add_customer_view,name='admin-add-customer'),
    path('admin-view-customer-booking', views.admin_view_customer_booking_view,name='admin-view-customer-booking'),
    path('delete-booking/<int:pk>', views.delete_booking_view,name='delete-booking'),
    path('cancel-ticket/<int:pk>', views.cancel_ticket_view,name='cancel-ticket'),


    path('admin-view-movie', views.admin_view_movie_view,name='admin-view-movie'),
    path('delete-movie/<int:pk>', views.delete_movie_view,name='delete-movie'),
    path('admin-view-released-movie', views.admin_view_released_movie_view,name='admin-view-released-movie'),
    path('admin-view-not-released-movie', views.admin_view_not_released_movie_view,name='admin-view-not-released-movie'),

    path('admin-view-producer', views.admin_view_producer_view,name='admin-view-producer'),
    path('delete-producer/<int:pk>', views.delete_producer_view,name='delete-producer'),
    path('admin-add-producer', views.admin_add_producer_view,name='admin-add-producer'),
    path('admin-view-producer-movie', views.admin_view_producer_movie_view,name='admin-view-producer-movie'),

    path('admin-view-distributor', views.admin_view_distributor_view,name='admin-view-distributor'),
    path('delete-distributor/<int:pk>', views.delete_distributor_view,name='delete-distributor'),
    path('admin-add-distributor', views.admin_add_distributor_view,name='admin-add-distributor'),
    path('admin-view-distributor-movie', views.admin_view_distributor_movie_view,name='admin-view-distributor-movie'),

    path('admin-view-theatre', views.admin_view_theatre_view,name='admin-view-theatre'),
    path('delete-theatre/<int:pk>', views.delete_theatre_view,name='delete-theatre'),
    path('admin-add-theatre', views.admin_add_theatre_view,name='admin-add-theatre'),
    path('admin-view-theatre-movie', views.admin_view_theatre_movie_view,name='admin-view-theatre-movie'),

    path('adminlogin', LoginView.as_view(template_name='multiplex/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-movie', views.admin_movie_view,name='admin-movie'),
    path('admin-add-movie', views.admin_add_movie_view,name='admin-add-movie'),
    path('admin-feedback', views.admin_feedback_view,name='admin-feedback'),
    path('admin-producer', views.admin_producer_view,name='admin-producer'),
    path('admin-approve-producer',views.admin_approve_producer_view,name='admin-approve-producer'),
    path('approve-producer/<int:pk>', views.approve_producer_view,name='approve-producer'),
    path('delete-producer/<int:pk>', views.delete_producer_view,name='delete-producer'),
    path('admin-theatre', views.admin_theatre_view,name='admin-theatre'),
    path('admin-approve-theatre',views.admin_approve_theatre_view,name='admin-approve-theatre'),
    path('approve-theatre/<int:pk>', views.approve_theatre_view,name='approve-theatre'),
    path('delete-theatre/<int:pk>', views.delete_theatre_view,name='delete-theatre'),
    path('admin-distributor', views.admin_distributor_view,name='admin-distributor'),
    path('admin-approve-distributor',views.admin_approve_distributor_view,name='admin-approve-distributor'),
    path('approve-distributor/<int:pk>', views.approve_distributor_view,name='approve-distributor'),
    path('delete-distributor/<int:pk>', views.delete_distributor_view,name='delete-distributor'),



    path('customer-home', views.customer_home_view,name='customer-home'),
    path('customer-dashboard', views.customer_dashboard_view,name='customer-dashboard'),
    path('customer-profile', views.customer_profile_view,name='customer-profile'),
    path('edit-customer-profile', views.edit_customer_profile_view,name='edit-customer-profile'),
    path('customer-feedback', views.customer_feedback_view,name='customer-feedback'),
    path('customer-ticket', views.customer_ticket_view,name='customer-ticket'),
    path('download-ticket', views.download_ticket_view,name='download-ticket'),
    path('download-tickets/<int:pk>', views.download_tickets_view,name='download-tickets'),
    path('view-movie-details/<int:pk>', views.view_movie_details_view,name='view-movie-details'),
    path('view-movie-detailss/<int:pk>', views.view_movie_detailss_view,name='view-movie-detailss'),

    path('book-now/<int:pk>', views.book_now_view,name='book-now'),
    path('choose-seat', views.choose_seat_view,name='choose-seat'),
    path('proceed-to-pay', views.proceed_to_pay_view,name='proceed-to-pay'),
    path('payment-success', views.payment_success_view,name='payment-success'),

    path('logout', LogoutView.as_view(template_name='multiplex/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
]
