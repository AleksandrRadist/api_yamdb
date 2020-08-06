from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


from .models import User
from .serializers import UsersSerializer
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

    def perform_create(self, serializer):
        serializer.save()


@api_view(['GET', 'PATCH'])
def get_current_user(request):
    user = request.user
    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = UsersSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
