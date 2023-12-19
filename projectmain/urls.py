from django.urls import path
from . import views


urlpatterns = [    
    path('', views.main_view, name='home'),
    path('maps/', views.map_view, name='maps'),
    path('santashohos/', views.santashohos_view, name='santashohos')

]