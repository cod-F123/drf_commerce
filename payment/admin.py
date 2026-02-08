from django.contrib import admin
from .models import Transaction

# Register your models here.

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'order',
        'transaction_status',
        'amount',
        'ref_id',
        'created_at'
    )

    list_filter = ('transaction_status', 'created_at')
    search_fields = ('ref_id', 'authority_id', 'order__order_id')

    readonly_fields = (
        'order',
        'amount',
        'ref_id',
        'authority_id',
        'transaction_status',
        'created_at',
    )

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj = ...):
        return False