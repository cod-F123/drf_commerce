from django.conf import settings

def get_payment_settings(setting, default=None):
    return settings.DRF_ECOMMERCE['PAYMENT'].get(setting, default)