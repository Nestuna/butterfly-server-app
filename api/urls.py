from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt

from api.views import ConversationMessagesResponse, ConversationResponse

urlpatterns = [
    path('conversation/', csrf_exempt(ConversationResponse.as_view())),
    path('conversation/message/', csrf_exempt(ConversationMessagesResponse.as_view()))
]

## URL type : conversation/?access_id=ihjgdoirg64646drhgdrhg