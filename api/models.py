from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from django.db.models.base import Model
from butterfly_api import settings
import datetime
import json


class Conversation(Model):
    access_id = models.CharField(max_length=32)
    creator_pseudo = models.CharField(max_length=32, null=True)
    lifespan = models.DurationField()

    users = models.ManyToManyField(User, related_name='users')

class Message(Model):
    # attributs
    username = models.CharField(max_length=32)
    date = models.DateField()
    text = models.CharField(max_length=200, null=True)

    # relations
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
