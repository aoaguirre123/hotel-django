from django.contrib import admin
from django.urls import path
from . import views
from hotel import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('servicio/', views.servicio, name='servicio'),
    path('servicio/crear/', views.crear_servicio, name='crear_servicio'),
    path('servicio/<int:servicio_id>/', views.detalle_servicio, name='detalle_servicio'),
    path('servicio/<int:servicio_id>/eliminar', views.eliminar_servicio, name='eliminar_servicio'),
    path('promocion/', views.promocion, name='promocion'),
    path('promocion/crear/', views.crear_promocion, name='crear_promocion'),
    path('promocion/<str:promocion_id>/', views.detalle_promocion, name='detalle_promocion'),
    path('promocion/<str:promocion_id>/eliminar', views.eliminar_promocion, name='eliminar_promocion'),
    
]