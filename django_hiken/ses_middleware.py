from django_ses import SESBackend
from django.conf import settings
from django.core.exceptions import ValidationError

class CustomSESBackend(SESBackend):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if not hasattr(settings, "SES_ACCESS_KEY_ID"):
            raise ValidationError("Missing SES_ACCESS_KEY_ID setting.")
        if not hasattr(settings, "SES_ACCESS_KEY"):
            raise ValidationError("Missing SES_ACCESS_KEY_ID setting.")
        
        self._access_key_id = settings.SES_ACCESS_KEY_ID
        self._access_key = settings.SES_ACCESS_KEY