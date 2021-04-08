"""
Definition of urls for StockEye.
"""

from datetime import datetime
from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
    path('', views.home, name='home'),
    path('watchlists/', views.watchlists, name='watchlists'),
    # Path for a user's specific Watchlist
    # Example: /watchlist/1/
    # This will display the user's watchlist with a watchlist_id of 1
    path('watchlist/<int:id>/', views.edit_watchlist, name='edit_watchlist'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
