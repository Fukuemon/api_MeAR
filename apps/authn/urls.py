from django.urls import path, include
from apps.authn import views
from rest_framework.routers import DefaultRouter
from djoser.views import UserViewSet


app_name = "user"

router = DefaultRouter()


# generics用
urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="register"),
    # ログインユーザーのアカウント削除のエンドポイント
    path('users/delete/', views.CustomUserViewSet.as_view(actions={'delete': 'delete_current_user'}), name='user-delete'),
    # パスワード変更のエンドポイント
    path('change_password/', UserViewSet.as_view(actions={'post': 'set_password'}), name='set-password'),
]