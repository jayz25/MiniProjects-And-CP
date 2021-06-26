from django.contrib import admin
from django.contrib import auth
from django.urls import path
from django.urls.resolvers import URLPattern
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
                path('',views.home, name="home"),
                path('customer/<str:pk>',views.customer, name="customer"),
                path('products/',views.products, name="products"),
                
                path('create_order/<str:pk>',views.createOrder, name="create_order"),
                path('update_order/<str:pk>',views.updateOrder, name="update_order"),
                path('delete_order/<str:pk>',views.deleteOrder, name="delete_order"),
                
                path('register/',views.registerPage, name="register"),
                path('login/',views.loginPage, name="login"),
                path('logout/',views.logoutUser, name="logout"),
                
                path('user_page',views.userPage, name="user_page"),
                path('account/',views.accountSettings, name="account"),
                
                path('reset_password/',
                    auth_views.PasswordResetView.as_view(template_name="Accounts/password_reset.html"), name="reset_password"), #Submit Email Form
                
                path('reset_password_sent/',
                    auth_views.PasswordResetDoneView.as_view(template_name="Accounts/password_reset_sent.html"), name="password_reset_done"), #Email sent success Message
                
                path('reset/<uidb64>/<token>/',
                    auth_views.PasswordResetConfirmView.as_view(template_name="Accounts/password_reset_form.html"), name="password_reset_confirm"), #Link to password reset form in email
                
                path('reset_password_complete/',
                    auth_views.PasswordResetCompleteView.as_view(template_name="Accounts/password_reset_done.html"), name="password_reset_complete"), #Password successfully changed message
                
    ]