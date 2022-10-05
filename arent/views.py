from django.shortcuts import render, redirect
from .models import Room
import folium
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User, Room, Items
from  django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm, ProfileForm, UploadForm, ItemsUploadForm
from django.core.mail import send_mail



# Homepage view
def index(request):
    sell_item = Items.objects.filter(type='SELL').first()
    lease_item = Items.objects.filter(type='LEASE').first()
    rooms = Room.objects.all().first()
    
    context = {'room': rooms, 'lease_item': lease_item, 'sell_item': sell_item}
    return render(request, "index.html", context)

# about-us papge
def about(request):
    context = {}
    return render(request, "about.html", context)

# contact-us page
def contact(request):
    if request.method == 'POST':
        sender = request.POST['email']
        subject = request.POST['subject']
        message = request.POST.get('message')
        
        send_mail(
            subject,
            message,
            sender,
            ['dezin.mj@gmail.com']
        )
    
    context = {}
    return render(request, "contact.html", context)

# services page
def service(request):
    context = {}
    return render(request, "services.html", context)

# page to buy items
def buypage(request):
    items = Items.objects.filter(type='SELL')
    
    context = {'items':items}        
    return render(request, "buy.html", context)

# page to upload items for sell
@login_required(login_url='login')
def sellpage(request):
    form = ItemsUploadForm()
    if request.method == 'POST':
        form = ItemsUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.seller = request.user
            form.save()
            return redirect('buy')
    
    context = {'form': form}
    return render(request, "sell.html", context)

# the page showing items for rent
def leasepage(request):
    items = Items.objects.filter(type='LEASE')
    
    context = {'items':items} 
    return render(request, "lease.html", context)

# page to confirm before permanently deleting an item 
def deletepage(request,pk):
    
    context = {}
    return render(request, "delete.html", context)

# the page showing the details of an item
def detailspage(request,pk):
    item_detail = Items.objects.get(id=pk)

    context = {'items':item_detail}
    return render(request, "items_detail.html", context)

# profile page
@login_required(login_url='login')
def profilepage(request, pk):
    profile = User.objects.get(id=pk)
    real_user = profile.email
    
    if request.user.email != real_user:
        return redirect('home')
    
    form = ProfileForm(instance=profile)
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form,'user':current_user}
    return render(request, "profile.html", context)

# a page to upload the location and detqails of a room
@login_required(login_url='login')
def uploadpage(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('search')
        
    rooms = Room.objects.all().values()
    cordinate = [7.785066, 4.546298]
    folium_map = folium.Map(location=cordinate, zoom_start=14).add_child(folium.LatLngPopup())
    # folium.TileLayer('Stamen Terrain').add_to(folium_map)
        
    locate = []
    # cordinates = []
    for room in rooms:
        lat = room['latitude']
        lng = room['longitude']
        locate.append(lat)
        locate.append(lng)
        # cordinates.append(locate)
        
        folium.Marker(locate, popup=f"<a href='http://127.0.0.1:8000/detail/{room['id']}/' target='_blank'>View room</a><br> "+room['name'],tooltip='click me!!').add_to(folium_map)
        
        locate = []
    
    mapping = folium_map._repr_html_()
        
    context = {'form': form, 'mapping': mapping}
    return render(request, "upload.html", context)

# the login page
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email= request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
            return redirect('login')
            
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password does not exist')
    context = {}
    return render(request,'login.html', context)

# logout page
def logoutuser(request):
    logout(request)
    return redirect('home')

# the registration page
def signuppage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = MyUserCreationForm()
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'an error occured during registration')
    
    context = {'form':form}
    return render(request, 'sign_up.html', context)


# a page to find rooms on a map
def search(request):
    rooms = Room.objects.all().values()
    cordinate = [7.785066, 4.546298]
    folium_map = folium.Map(location=cordinate, zoom_start=14).add_child(folium.LatLngPopup())
    # folium.TileLayer('stamenterrain',attr='quest').add_to(folium_map)
        
    locate = []
    # cordinates = []
    for room in rooms:
        lat = room['latitude']
        lng = room['longitude']
        locate.append(lat)
        locate.append(lng)
        # cordinates.append(locate)
        
        folium.Marker(locate, popup=f"<a href='http://127.0.0.1:8000/detail/{room['id']}/' target='_blank'>View room</a><br> "+room['name'],tooltip='click me!!').add_to(folium_map)
        
        locate = []
    
    mapping = folium_map._repr_html_()
    context = {'mapping':mapping}
    return render(request, "search.html", context)

# the page showing the details of a room
def details(request,pk):
    room_detail = Room.objects.get(id=pk)

    context = {'room':room_detail}
    return render(request, "details.html", context)