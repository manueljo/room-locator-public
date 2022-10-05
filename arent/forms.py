from  django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Room, Items

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'mobile_number', 'bio', 'permanent_address', 'residential_address', 'lga', 'nin_number', 'avatar']
        
class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)
    message = forms.CharField(widget=forms.Textarea,max_length=2000)
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'permanent_address', 'mobile_number', 'bio', 'residential_address', 'lga', 'nin_number', 'avatar']
        
class UploadForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        
        exclude = ['available']
        
class ItemsUploadForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = '__all__'
        
        exclude = ['seller']