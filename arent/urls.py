from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('buy/', views.buypage, name='buy'),
    path('sell/', views.sellpage, name='sell'),
    path('lease/', views.leasepage, name='lease'),
    path('delete_item/<int:pk>/', views.deletepage, name='delete_item'),
    path('items_detail/<int:pk>/', views.detailspage, name='items_detail'),
    path('profile/<int:pk>/', views.profilepage, name='profile'),
    path('uploads/', views.uploadpage, name='upload'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.service, name='service'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('signup/', views.signuppage, name='signup'),
    path('detail/<int:pk>/', views.details, name='room-detail'),
]