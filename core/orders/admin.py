from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemInlineAdmin(admin.StackedInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user__email','total_amount','order_status','created_at']
    search_fields = ['order_is','user__email','user__username']
    list_filter = ['order_status']
    
    
    fieldsets = (
        (None, {'fields':['user','order_id','total_amount']}),
        ('shiping address',{'fields':['address','zip_code']}),
        ('Status and Important dates', {'fields': ['order_status','created_at','payed_at','shipped_at']})
    )
    
    
    readonly_fields = ['order_id','created_at','payed_at','shipped_at']
    inlines = [OrderItemInlineAdmin]