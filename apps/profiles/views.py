from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets

from .models import Profile, Connection
from . import serializers


# プロフィールのCRUD操作を行うViewSet
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(userProfile=self.request.user)


# 自身のプロフィールを返すListView
class MyProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    def get_queryset(self):
        return self.queryset.filter(userProfile=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_id=None):
    user = request.user
    following_id = request.data.get('following_id', user_id)
    target_user = get_object_or_404(Profile, id=following_id)

    if user == target_user:
        return Response({"detail": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

    if Connection.objects.filter(follower=user.profile, following=target_user.profile).exists():
        return Response({"detail": "Already following."}, status=status.HTTP_400_BAD_REQUEST)

    Connection.objects.create(follower=user.profile, following=target_user.profile)
    return Response({"detail": "Follow successful"}, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def unfollow(request, user_id=None):
    user = request.user
    following_id = request.data.get('following_id', user_id)
    target_user = get_object_or_404(Profile, id=following_id)

    try:
        connection = Connection.objects.get(follower=user.profile, following=target_user.profile)
        connection.delete()
        return Response({"detail": "Unfollow successful"}, status=status.HTTP_200_OK)
    except Connection.DoesNotExist:
        return Response({"detail": "Connection does not exist."}, status=status.HTTP_400_BAD_REQUEST)