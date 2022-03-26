from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path("products/<int:myid>", views.products, name="ProductView"),
    path('contact/', views.contact, name="Contact"),
    path('about/', views.about, name='About'),
    path('search/', views.search, name="Search"),
    path('tracker/', views.Tracker, name="Tracker"),
    path('checkout/', views.CheckOut, name="CheckOut"),
    path('thanksforshoppingwithus/<int:orderid>', views.ordered,
         name="ThanksForShoppingWithUs")

]
