from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),

    path('register/', views.RegisterUserApi.as_view()),
    path('update-username/<str:email>/', views.UpdateUsernameApi.as_view()),
    path('change-password/<str:email>/', views.ChangePasswordUserApi.as_view()),
    path('update-info/<str:email>/', views.UpdateUserInfoApi.as_view()),
    path('user/<str:email>/', views.UserDetailApi.as_view()),
    
    path('address/', views.AddAndListUserAddressApi.as_view()),
    path('address/<int:id>/', views.DetailAndUpdateAndDeleteUserAddressApi.as_view()),
    
]
