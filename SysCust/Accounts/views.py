from Accounts.decorators import unauthenticated_user
from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.forms import formsets, inlineformset_factory #to get multiple form inputs into database simultaneously
from .filters import OrderFilter #Creating custom search bar to filter elements
from .models import *
from .forms import CustomerForm, OrderForm, CreateUserForm #Creating Order Customer form page
from django.contrib.auth.forms import UserCreationForm #Creating Login And Regiter Page
from django.contrib import messages #Flashing Messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout #User login logout authentication
from django.contrib.auth.decorators import login_required #For User specific pages 
from .decorators import admin_only, allowed_users, unauthenticated_user #Adding decorators which we created
# Create your views here.


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            #group = Group.objects.get(name = 'customer')
            #user.groups.add(group)
            '''Customer.objects.create(
                user = user,
            )'''

            messages.success(request, 'Account was successfully created for ' + username)
            return redirect('login')

    contextDict = {'form':form}
    return render(request, 'Accounts/register.html', contextDict)


@unauthenticated_user
def loginPage(request):
    contextDict = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password does not match")
            return render(request, 'Accounts/login.html', contextDict)
    return render(request, 'Accounts/login.html',contextDict)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()   
    contextDict = {'form':form}
    return render(request, 'Accounts/account_settings.html',contextDict)


@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    contextDict = {
        'orders':orders, 'customers':customers,'total_orders':total_orders,
        'total_customers':total_customers,'delivered':delivered,'pending':pending
    }
    
    return render(request,'Accounts/dashboard.html',contextDict)
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    contextDict = {'orders':orders,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request, 'Accounts/user.html',contextDict)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return render(request,'Accounts/products.html',{'productsDICT':products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    orderFilter = OrderFilter(request.GET, queryset=orders)
    orders  = orderFilter.qs
    
    contextDict = {'customer':customer,'orders':orders,'order_count':order_count,'orderFilter':orderFilter}
    return render(request,'Accounts/customer.html',contextDict)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product','status'),extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset = Order.objects.none(),instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    contextDict = {'formset':formset}
    return render(request,'Accounts/order_form.html',contextDict)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request,pk):
    order = Order.objects.get(id=pk)

    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    contextDict = {'form':form}
    return render(request, 'Accounts/order_form.html',contextDict)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    contextDict = {'item':order}
    return render(request,'Accounts/delete.html',contextDict)