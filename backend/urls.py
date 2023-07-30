from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView  # To use TemplateView for React views
from . import views
from .views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),
    path('staff/', views.staff , name='staff'),
    path('report/', views.report, name='report'),
    path('login/', login_view.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]