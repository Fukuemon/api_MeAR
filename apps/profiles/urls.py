from django.urls import path, include
from apps.profiles import views
from rest_framework.routers import DefaultRouter

app_name = "profile"

router = DefaultRouter()
router.register("profile", views.ProfileViewSet)

urlpatterns=[
    path("myprofile/", views.MyProfileListView.as_view(), name="myprofile"),
    path('<slug:username>/follow', views.FollowView.as_view(), name='follow'),
    path('<slug:username>/unfollow', views.UnfollowView.as_view(), name='unfollow'),
    path("",include(router.urls)),
]

