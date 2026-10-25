from django.contrib import admin
from .models import Category , Product, ImageProduct

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    
    
class ImageProductInlineAdmin(admin.StackedInline):
    model = ImageProduct
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category__name","price","percent_off","is_exist"]
    list_editable = ["price", "percent_off", "is_exist"]
    search_fields = ["name", "category__name"]
    list_filter = ["category__name", "is_exist"]
    
    readonly_fields = ["date_added", "slug"]
    inlines = [ImageProductInlineAdmin]
    