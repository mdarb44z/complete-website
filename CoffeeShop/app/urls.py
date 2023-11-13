from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('',views.index,name='app'),
    path('about',views.about,name='about'),
    path('menu',views.menu,name='menu'),
    path('products',views.products,name='products'),
    path('review',views.review,name='review'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('login',views.handlelogin,name='handlelogin'),
    path('signup',views.signup,name='signup'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('about2',views.about2,name='about2'),
    path('payment',views.payment,name='payment')
    

]
