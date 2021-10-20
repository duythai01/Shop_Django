from django.urls import path, include
from rest_framework import routers
from drf_registration import api
from . import views

router = routers.DefaultRouter()
# router.register("users", views.CustomerUserViewSet, 'user')
# router.register("buyer.register", views.RegisterView, 'register')
# router.register("login", views.LoginView.as_view(), 'login')


urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info', views.AuthInfo.as_view()),

]
