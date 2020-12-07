from django.contrib import admin
from django.urls import path, include
from api.views import Login
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('login/<int:user_id>', csrf_exempt(Login.as_view()), name='test')
]