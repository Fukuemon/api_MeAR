from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

#ユーザーモデルのベースとなるクラスを作成
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("メールアドレスを設定してください")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)


        return user

    # スーパーユーザーの作成
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff=True  # admin権限
        user.is_superuser = True # 全ての権限
        user.save(using=self._db) # データベースに保存


        return user

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager() # UserManagerのインスタンスを生成

    USERNAME_FIELD = "email" # 認証のためのフィールドをデフォルトのusernameからemailに変更

    def __str__(self):
        return self.email




