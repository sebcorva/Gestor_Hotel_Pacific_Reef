from django.urls import path
from .views import catalogo, home, exit, register

urlpatterns = [
    path('', catalogo, name="catalogo"),
    path('home/', home, name="home"),
    path('logout/', exit, name="exit"),
    path('register/', register, name="register"),
]
