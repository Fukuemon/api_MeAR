from rest_framework import serializers
from .models import Profile, Connection

class ProfileSerializer(serializers.ModelSerializer):

    created_on = serializers.DateTimeField(format="%Y^%m-%d", read_only=True)
    class Meta:
        model = Profile
        fields = "__all__"
        extra_kwargs = {"userProfile":{"read_only":True}}

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = "__all__"