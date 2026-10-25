from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateAndListOrderApi.as_view()),
    path('<str:order_id>/', views.DetailAndDeleteOrderApi.as_view()),
]
