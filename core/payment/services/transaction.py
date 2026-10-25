from django.db import transaction as transaction_db
from payment.models import Transaction

@transaction_db.atomic
def mark_transaction_success(transaction:Transaction, ref_id: str):
    if transaction.transaction_status == 'SUCCESS':
        return transaction
    
    transaction.transaction_status = 'SUCCESS'
    transaction.ref_id = ref_id
    transaction.save(update_fields=['transaction_status', 'ref_id'])
    
    order = transaction.order 
    order.order_status = 'Payed'
    order.save(update_fields = ['order_status'])
    
    return transaction