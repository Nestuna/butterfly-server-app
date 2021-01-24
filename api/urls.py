from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt

from api.views import ConversationMessagesResponse, ConversationResponse, Login, ConversationUser

urlpatterns = [
    path('login/', csrf_exempt(Login.as_view())),
    path('login/<str:username/', csrf_exempt(Login.as_view())),
    path('conversation/', csrf_exempt(ConversationResponse.as_view())),
    path('conversation/message/', csrf_exempt(ConversationMessagesResponse.as_view())),
    path('conversationuser/', csrf_exempt(ConversationUser.as_view()))
]
