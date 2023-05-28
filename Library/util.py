from django.contrib.auth.models import *

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['authenticated'] = self.request.user.is_authenticated
        return context