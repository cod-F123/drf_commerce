from django.shortcuts import render , redirect
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from orders.models import Order 
from .models import Transaction
from .services.transaction import mark_transaction_success
from .utils import get_payment_settings

# Create your views here.

CALLBACK_URL = get_payment_settings('CALLBACK_URL')


class StartToTransaction(APIView):
    
    permission_classes = [IsAuthenticated,]    

    def post(self, request, order_id, format=None):
        
        order = Order.objects.filter(order_id = order_id, user = request.user, order_status = 'Pending').first()
        
        if order is None:
            return Response({"Error":"Order not Found !"},status=status.HTTP_404_NOT_FOUND)
        
        
        
        # Youre Transaction Method and Peyment Gateway
        
        
        authority_id = "get authority form peymentgetway"
        
        transaction , created = Transaction.objects.get_or_create(order = order )
        
        if transaction.transaction_status == 'SUCCESS':
            return Response(
                {"error": "Order already paid"},
                status=status.HTTP_400_BAD_REQUEST
            )
        transaction.authority_id = authority_id
        transaction.save(update_fields = ['authority_id'])
        
        
        payment_url = "get payment url from getway"
        
        return Response(data={"payent_url" : payment_url},status=status.HTTP_201_CREATED)
    


class CallbackPaymentGetway(APIView):
    
    authentication_classes = []
    permission_classes = []
        
    def get(self, request, format=None):
        
        fail_url = get_payment_settings('FAIL_URL')
        success_url = get_payment_settings('SUCCESS_URL')
        
        
        # Youre Check payment status
        
        # get authority and check Transaction and ...
        
        authority_id = """ get authority from request.GET """
        status_param = "get status from request.GET"
        
        if not authority_id:
            return redirect(fail_url)
        
        transaction = Transaction.objects.filter(authority_id = authority_id).first()
        
        if transaction  is None:
            
            return redirect(fail_url)
        
        if transaction.transaction_status == 'SUCCESS':
            return redirect(success_url)
        
        if status_param != 'OK':
            return redirect(fail_url)
            
        
        # verify peyment
        
        # youre verify action
        
        # if payemnt successfuly use mark_transaction_success for change status
        
        ref_id = "get_ref_id from verify_payemnt"
        
        try:
            mark_transaction_success(transaction, ref_id)
        except Exception:
            return redirect(fail_url)
        
        
        return redirect(success_url)