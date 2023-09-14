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
    created_on = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(blank=True, null=True, upload_to=upload_avatar_path)

# フォローフォロワー機能
class Connection(models.Model):
    follower = models.ForeignKey(Profile, related_name="follower", on_delete=models.CASCADE)
    following = models.ForeignKey(Profile, related_name='following', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} : {}".format(self.follower.nikeName, self.following.nikeName)
