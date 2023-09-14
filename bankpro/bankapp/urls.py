from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('newpage',views.newpage,name="newpage"),
    path('application',views.application,name="application"),
]
