from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import connexion, register, deconnexion, add_user, delete_user, list_users, UserProfileView, update_user

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('connexion/', connexion, name='connexion'),
    path('register/', register, name='register'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path('add_user/', add_user, name='add_user'),
    path('delete_user/<str:username>/', delete_user, name='delete_user'),
    path('list_users/', list_users, name='list_users'),
    path('update_user/<str:username>/', update_user, name='update_user'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
