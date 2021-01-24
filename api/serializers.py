from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from .models import Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        
class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['access_id', 'creator_pseudo', 'lifespan']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['username', 'date', 'text']