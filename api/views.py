# django
from django.db.utils import IntegrityError
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
# utils
from api.serializers import ConversationSerializer, MessageSerializer, UserSerializer
import uuid
import datetime
import json
# models
from django.contrib.auth.models import User
from .models import Conversation, Message


class ConversationResponse(View):
    def get(self, request):
        try:
            access_id = request.GET.get('access_id')
            conversation = Conversation.objects.get(access_id=access_id)
            serializer = ConversationSerializer(conversation)
            return JsonResponse(serializer.data, status=200)
        except Exception as e:
            print('ConversationResponse GET : ', e)
            return HttpResponse(status=400)

    def post(self, request):
        try:
            json_conversation = request.body.decode("utf-8")
            dict_conversation = json.loads(json_conversation)
            access_id = uuid.uuid4().hex

            Conversation.objects.create(
                access_id = access_id,
                creator_pseudo = dict_conversation['pseudo'],
                lifespan = datetime.timedelta(days=int(dict_conversation['lifespan'])),
            )
            return HttpResponse(access_id, status=200)
        except Exception as e:
            print('ConversationResponse POST : ', e)
            return HttpResponse(status=500)

    def delete(self, request):
        try:
            conversation_json = request.body.decode('utf-8')
            conversation_dict = json.loads(conversation_json)
            access_id = conversation_dict['conversationAccessId']
            conversation = Conversation.objects.get(access_id=access_id)
            conversation.delete()
            return HttpResponse(status=200)
        except Exception as e:
            print('ConversationResponse DELETE : ', e)
            return HttpResponse(status=500)

class ConversationMessagesResponse(View):
    def get(self, request):
        try:
            access_id = request.GET.get('access_id')
            conversation = Conversation.objects.get(access_id=access_id)
            conversation_data = ConversationSerializer(conversation).data

            messages = Message.objects.filter(conversation_id=conversation.id)
            messages_list = []
            for message in messages:
                message_data = {
                    'id': message.id,
                    'username': message.username,
                    'date': str(message.date),
                    'text': message.text
                }
                messages_list.append(message_data)

            conversation_messages = {**conversation_data, 'messages': messages_list}

            return JsonResponse(messages_list, status=200)
        except Exception as e:
            print('ConversationMessagesResponse GET : ', e)
            return JsonResponse({}, status=400)

    def post(self, request):
        try:
            request_body = request.body.decode("utf-8")
            message = json.loads(request_body)
            print(message)
            access_id = message['access_id']

            Message.objects.create(
                username = message['username'],
                date = datetime.date.today(),
                text = message['text'],
                conversation_id = Conversation.objects.get(access_id=access_id).id
            )
            return HttpResponse(status=200)
        except Exception as e:
            print('ConversationMessagesResponse POST: ', e)
            return HttpResponse(status=400)


class Login(View):
    def get(self, request, user_id, username):
        try:
            user = User.objects.get(username=username)
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

