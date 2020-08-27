from rest_framework import viewsets, permissions, status, mixins
from rest_framework.decorators import api_view, action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator

from .models import User
from .serializers import UsersSerializer, EmailSerializer
from .permissions import IsStaff


class UsersViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    permission_classes = (
        permissions.IsAuthenticated,
        IsStaff,
    )
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    pagination_class = PageNumberPagination

    @action(detail=True, permission_classes=[permissions.IsAuthenticated])
    @api_view(['GET', 'PATCH'])
    def get_current_user(request):
        user = request.user
        if request.method == 'GET':
            serializer = UsersSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PATCH':
            serializer = UsersSerializer(user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)


class EmailViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    @action(detail=False, methods=['post'], url_path='email')
    def send_confirmation_code(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, created = User.objects.get_or_create(
            email=serializer.data.get('email')
        )
        if created:
            user.username = serializer.data.get('email')
            user.save()

        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            'Confirm your account',
            confirmation_code,
            'smtp.gmail.com',
            [user],
            fail_silently=False,
        )
