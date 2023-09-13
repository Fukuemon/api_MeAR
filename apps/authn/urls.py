from django.urls import path, include
from apps.authn import views
from rest_framework.routers import DefaultRouter

app_name = "user"

router = DefaultRouter()

# generics用
urlpatterns = [
    path("register/", views.CreateUserView.as_view(), name="register"),
    path("",include(router.urls))
]