from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerForm(ModelForm): #For customizing profile pic, profile details
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class OrderForm(ModelForm): #Order Form creation inhereting ModelForm, Copying all the fields from Order this will help in project to input multiple orders in customer section
    class Meta:
        model = Order
        fields = '__all__'

class CreateUserForm(UserCreationForm): #Creating a User form with some custom fields inhereting from UserCreation Default form
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2'] #Read Documentation for these fields
        