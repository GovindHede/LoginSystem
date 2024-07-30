from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('forgot/', views.forgot, name='forgot'),
    path('welcome/', views.welcome, name='welcome'),
]
