from django.urls import path
from app.view.ContainerView import ContainerView
from app.view.ProductView import ProductView
from app.view.ClientView import ClientView
from app.view.UserView import UserView
from app.view.TruckView import TruckView
from app.view.LoginView import LoginView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('container/', ContainerView.as_view(), name='container_list'),
    path('container/<str:id>', ContainerView.as_view(), name='container_process'),
    path('product/', ProductView.as_view(), name='product_list'),
    path('product/<str:id>', ProductView.as_view(), name='product_process'),
    path('client/', ClientView.as_view(), name='product_list'),
    path('client/<str:id>', ClientView.as_view(), name='product_process'),
    path('user/', UserView.as_view(), name='user'),
    path('user/<str:id>', UserView.as_view(), name='user_list'),
    path('register/user/', UserView.as_view(), name='user_register'),
    path('login/', LoginView.as_view(), name='login'),
    path('truck/', TruckView.as_view(), name='truck'),
    path('truck/<str:id>', TruckView.as_view(), name='trucks')
]
