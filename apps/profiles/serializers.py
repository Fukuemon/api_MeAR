from rest_framework import serializers
from .models import Profile, Connection

# プロフィールの一部のフィールドを扱うためのシリアライザー
class ProfileBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['nickName', 'created_on', 'img']

# フォロー機能のシリアライザー
class ConnectionSerializer(serializers.ModelSerializer):
    follower = ProfileBriefSerializer(source='follower', read_only=True)
    following = ProfileBriefSerializer(source='following', read_only=True)

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
        following_profiles = [connection.following for connection in followings]
        return ProfileBriefSerializer(following_profiles, many=True).data

    def get_followers(self, obj):
        # プロフィールをフォローしている人をシリアライズ
        followers = Connection.objects.filter(following=obj)
        follower_profiles = [connection.follower for connection in followers]
        return ProfileBriefSerializer(follower_profiles, many=True).data



