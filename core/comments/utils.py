from django.conf import settings

def get_comment_setting(setting,default=None):
    return settings.DRF_ECOMMERCE["COMMENTS"].get(setting, default)