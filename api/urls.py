from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt

from .views import Login, ConversationResponse

urlpatterns = [
    path('login/', csrf_exempt(Login.as_view()), name='login'),
    path('login/<int:user_id>', csrf_exempt(Login.as_view()), name='login'),
    path('conversation/', csrf_exempt(ConversationResponse.as_view())),
]

## URL type : conversation/?access_id=ihjgdoirg64646drhgdrhg