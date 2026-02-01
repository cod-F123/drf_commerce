from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateCommentApi.as_view()),
    path('delete/<int:id>/', views.DeleteCommentApi.as_view()),
    path('update/<int:id>/', views.UpdateCommentApi.as_view()),
]
