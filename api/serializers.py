from api.models import Conversation
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from api.models import Conversation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['access_id', 'nb_users', 'lifespan']