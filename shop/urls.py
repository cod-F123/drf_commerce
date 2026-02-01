from django.urls import path
from . import views


urlpatterns = [
    path('category-list/', views.CategoryListApi.as_view()),
    path('product-list/', views.ProductListApi.as_view()),
    path('product/<str:slug>/', views.ProductDetailApi.as_view()),
]
