from django.urls import path, include
from rest_framework import routers

from user import views

router = routers.DefaultRouter()
router.register("users", views.CustomerUserViewSet, 'user')


urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info', views.AuthInfo.as_view())

]