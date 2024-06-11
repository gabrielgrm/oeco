from django.urls import path
from . import views
from .views import login_view


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login_view, name='login'),
]