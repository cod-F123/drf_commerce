from django.urls import path
from . import views

urlpatterns = [
    path('start/<str:order_id>/', views.StartToTransaction.as_view()),
    path('callback-payment/', views.CallbackPaymentGetway.as_view()),
]
