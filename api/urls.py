from django.contrib import admin
from django.urls import path, include, re_path
from api.views import Login
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path(r'login/', csrf_exempt(Login.as_view()), name='login'),
    path(r'login/<int:user_id>', csrf_exempt(Login.as_view()), name='login')
]