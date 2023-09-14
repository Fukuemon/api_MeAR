from rest_framework import serializers
from .models import Profile, Connection

# フォロー機能のシリアライザー
class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['follower', 'following']


# プロフィールモデルにフォローとフォロワーを格納する
class ProfileSerializer(serializers.ModelSerializer):
    followings = ConnectionSerializer(many=True, read_only=True)
    followers = ConnectionSerializer(many=True, read_only=True)
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Profile
        fields = ['nickName', 'userProfile', 'created_on', 'img', 'followings', 'followers']
        extra_kwargs = {"userProfile": {"read_only": True}}

