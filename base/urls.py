from django.urls import path, include
from django.contrib import admin
from base import views

app_name='base'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('index/', views.index, name='index'),

    path('login/', views.login, name='login'),
    path('join/', views.join, name='join'),
    path('logout/', views.logout, name='logout'),

]