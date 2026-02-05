from django.conf import settings

def get_payment_settings(setting, default):
    return settings.DRF_ECOMMERCE['PAYMENT'].get(setting, default)