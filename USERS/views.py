from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Poste
from .serializers import UserSerializer, PosteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView

@api_view(['POST'])
def connexion(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            try:
                user_profile = user.poste
                poste = user_profile.poste
            except user.poste.DoesNotExist:  
                return Response("Vous devez avoir un poste", status=status.HTTP_400_BAD_REQUEST)

            if poste == 'ADMINISTRATEUR':
                login(request, user)
                return Response(status=status.HTTP_200_OK)

            elif poste == 'UTILISATEUR':
                login(request, user)
                return Response(status=status.HTTP_200_OK)

            else:
                return Response('Vous devez avoir un poste valide', status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response("Mot de passe ou nom d'utilisateur incorrect", status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Utilisateur non trouvé", status=status.HTTP_404_NOT_FOUND)

    user_serializer = UserSerializer(user, data=request.data, partial=True)
    if user_serializer.is_valid():
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print(user)
        user_data = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "poste":user.poste.poste
            
            # Ajoutez d'autres champs de l'utilisateur ici si nécessaire
        }
        return Response(user_data)

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        poste_serializer = PosteSerializer(data=request.data)
        if user_serializer.is_valid() and poste_serializer.is_valid():
            user = user_serializer.save()
            poste = poste_serializer.save(user=user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def deconnexion(request):
    if request.method == 'GET':
        logout(request)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_user(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        poste_serializer = PosteSerializer(data=request.data)
        if user_serializer.is_valid() and poste_serializer.is_valid():
            user = user_serializer.save()
            poste = poste_serializer.save(user=user)
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def delete_user(request, username):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(username=username)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response("Utilisateur non trouvé", status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def list_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)





@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, username):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(username=username)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response("Utilisateur non trouvé", status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
