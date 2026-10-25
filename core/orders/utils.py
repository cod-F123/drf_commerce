from django.conf import settings

def get_order_settings(setting, default= None):
    return settings.DRF_ECOMMERCE['ORDERS'].get(setting, default)