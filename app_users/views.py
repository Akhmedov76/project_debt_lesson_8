from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import UserModel
from .serializers import *


@api_view(['POST'])
def register_user_view(request):
    if request.method == 'POST':
        data = request.data
        serializer = RegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_user_view(request):
    if request.method == 'POST':
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


# for admin
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_user_view(request):
    users = UserModel.objects.all()
    search_query = request.query_params.get('search', None)
    page = int(request.query_params.get('page', 1))
    paginator = int(request.query_params.get('paginator', 10))
    if page is not None:
        page -= 1
        users = users[page * paginator:page * paginator + paginator]

    if search_query is not None:
        if search_query.isdigit():
            users = users.filter(phone_number__search=search_query)
        else:
            users = users.filter(username__icontains=search_query)

    serializer = UserModelSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_user_by_id_view(request, pk):
    user = UserModel.objects.get(id=pk)
    serializer = UserModelSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
