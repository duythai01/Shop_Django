from django.conf import settings

from django.shortcuts import render

from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import CustomerUser
from user.serializer import CustomerUserSerializer


class CustomerUserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = CustomerUser.objects.filter(is_active=True)
    serializer_class = CustomerUserSerializer

    def get_permissions(self):
        if self.action == 'get_current_user':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path='current_user')
    def get_current_user(self, request):
        return Response(self.serializer_class(request.user).data,
                        status=status.HTTP_200_OK)


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INF, status=status.HTTP_200_OK)
