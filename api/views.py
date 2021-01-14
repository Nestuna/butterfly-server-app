# django
from django.db.utils import IntegrityError
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
# utils
from api.serializers import UserSerializer, ConversationSerializer
import json
import uuid
import datetime
# models
from django.contrib.auth.models import User
from api.models import Conversation


class Login(View):
    def get(self, request, user_id, prenom):
        try:
            user = User.objects.get(pk=user_id)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)
        except User.DoesNotExist:
            return HttpResponse('User doesn\'t exist', status=404)
        else:
            print('Login.get() : ', Exception)
            return HttpResponse(status=400)

    def post(self, request):
        json_user = request.body.decode("utf-8")
        dict_user = json.loads(json_user)
        try :
            new_user = User.objects.create_user(dict_user['username'], dict_user['email'], dict_user['password'])
            new_user.save()
            return HttpResponse(status=200)
        except IntegrityError as e:
            message = 'Breaking DB Constraint: Probably, user already exists'
            return HttpResponse(message, status=401)
        except Exception as e:
            print('Login POST : ', e)
            return HttpResponse(status=500)

class ConversationResponse(View):
    def get(self, request):
        try:
            access_id = request.GET.get('access_id')
            conversation = Conversation.objects.get(access_id=access_id)
            serializer = ConversationSerializer(conversation)
            return JsonResponse(serializer.data)
        except Exception as e:
            print('ConversationResponse GET : ', e)
            return HttpResponse(status=400)

    def post(self, request):
        try:
            json_conversation = request.body.decode("utf-8")
            dict_conversation = json.loads(json_conversation)

            Conversation.objects.create(
                access_id = uuid.uuid1().hex,
                lifespan = datetime.timedelta(days=int(dict_conversation['lifespan'])),
                nb_users = int(dict_conversation['nb_users'])
            )
            return HttpResponse(status=200)   
        except Exception as e:
            print('ConversationResponse POST : ', e)
            return HttpResponse(status=500)

