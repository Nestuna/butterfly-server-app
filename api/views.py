from django.db.utils import IntegrityError
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from api.serializers import UserSerializer
import json

# Create your views here.
class Login(View):
    def get(self, request, user_id):
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
            print('Login.post() : ', e)
            return HttpResponse(status=400)