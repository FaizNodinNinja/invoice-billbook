from django.contrib.auth.backends import ModelBackend

class FrontendAuthBackend(ModelBackend):
    """
    This backend is ONLY for login.html frontend login.
    Admin panel cannot detect or use this backend.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        if request is None:
            return None
        return super().authenticate(request, username=username, password=password)
