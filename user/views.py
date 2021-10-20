from django.conf import settings
from django.contrib.auth.models import update_last_login

from django.shortcuts import render

from drf_registration.settings import drfr_settings
from drf_registration.utils.common import import_string, import_string_list
from drf_registration.utils.users import get_user_profile_data
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomerUser


# class CustomerUserViewSet(viewsets.ViewSet, generics.CreateAPIView):
#     queryset = CustomerUser.objects.filter(is_active=True)
#     serializer_class = CustomerUserSerializer
#
#     def get_permissions(self):
#         if self.action == 'get_current_user':
#             return [permissions.IsAuthenticated()]
#
#         return [permissions.AllowAny()]
#
#     @action(methods=['get'], detail=False, url_path='current_user')
#     def get_current_user(self, request):
#         return Response(self.serializer_class(request.user).data,
#                         status=status.HTTP_200_OK)


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INF, status=status.HTTP_200_OK)

#
# class LoginView( CreateAPIView):
#     """
#     This is used to Login into system.
#     """
#
#     permission_classes = import_string_list(drfr_settings.LOGIN_PERMISSION_CLASSES)
#     serializer_class = import_string(drfr_settings.LOGIN_SERIALIZER)
#
#     def post(self, request, *args, **kwargs):
#         """
#         Override to check user login
#         Args:
#             request (object): The request object
#         """
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         user = serializer.validated_data['user']
#
#         # Update last logged in
#         update_last_login(None, user)
#         data = get_user_profile_data(user)
#
#         return Response(data, status=status.HTTP_200_OK)
