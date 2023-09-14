from django.db import models
# Create your models here.
from django.conf import settings
def upload_avatar_path(instance, filename):
    ext = filename.split('.')[-1]

    # 保存先のファイルパスを生成
    # 生成されたファイルパスは 'avatars/{ユーザープロファイルのID}{ニックネーム}.{拡張子}'という形式になる
    return '/'.join(['avatars', str(instance.userProfile.id) + str(instance.nickName) + str(".") + str(ext)])


# プロフィール
class Profile(models.Model):
    nickName = models.CharField(max_length=20 ,null=True, blank=True)
    # Userモデルとリレーション
    userProfile = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profile',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)  # 作成日
    img = models.ImageField(blank=True, null=True, upload_to=upload_avatar_path)  # アバター画像

    # フォロー関連のフィールド
    followings = models.ManyToManyField(
        'User', verbose_name='フォロー中のユーザー', through='Connection',
        related_name='+', through_fields=('follower', 'following')
    )
    followers = models.ManyToManyField(
        'User', verbose_name='フォローされているユーザー', through='Connection',
        related_name='+', through_fields=('following', 'follower')
    )

# フォロー/フォロワー機能
class Connection(models.Model):
    follower = models.ForeignKey("User", on_delete=models.CASCADE, related_name="following_connection")
    following = models.ForeignKey('User', on_delete=models.CASCADE, related_name='follower_friendships')
    class Meta:
        unique_together = ('follower', 'following')
