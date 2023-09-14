from rest_framework import serializers
from .models import Profile, Connection

# フォロー機能のシリアライザー
class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['follower', 'following']


# プロフィールモデルにフォローとフォロワーを格納する
class ProfileSerializer(serializers.ModelSerializer):
    followings = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Profile
        fields = ['nickName', 'userProfile', 'created_on', 'img', 'followings', 'followers']
        extra_kwargs = {"userProfile": {"read_only": True}}

    def get_followings(self, obj):
        # プロフィールがフォローしている人をシリアライズ
        followings = Connection.objects.filter(follower=obj)
        return ConnectionSerializer(followings, many=True).data

    def get_followers(self, obj):
        # プロフィールをフォローしている人をシリアライズ
        followers = Connection.objects.filter(following=obj)
        return ConnectionSerializer(followers, many=True).data


