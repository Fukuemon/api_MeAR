from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from . import serializers
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import User
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)



class CustomUserViewSet(DjoserUserViewSet):

    # ログイン中のユーザー削除のエンドポイント
    @action(detail=False, methods=['DELETE'])
    def delete_current_user(self, request):
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
