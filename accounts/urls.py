
from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('lista-usuarios/', views.lista_de_usuarios, name='lista-usuarios'),
]