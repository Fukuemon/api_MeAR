from django.urls import path, include
from apps.profiles import views
from rest_framework.routers import DefaultRouter

app_name = "profile"

router = DefaultRouter()
router.register("profile", views.ProfileViewSet)

urlpatterns=[
    path("myprofile/", views.MyProfileListView.as_view(), name="myprofile"),
    path("follow/", views.follow, name="follow"),
    path("unfollow", views.unfollow, name="unfollow"),
    path("",include(router.urls)),
]

