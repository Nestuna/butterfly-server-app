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
    
