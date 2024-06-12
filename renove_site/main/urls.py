from django.urls import path
from . import views
from .views import login_view, home_view, view_appointments, new_appointment


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('appointments/', views.view_appointments, name='view_appointments'),
    path('appointments/new/', views.new_appointment, name='new_appointment'),
    path('comprovante/', views.comprovante, name='comprovante'),
]