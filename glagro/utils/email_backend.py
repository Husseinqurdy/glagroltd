import ssl
from django.core.mail.backends.smtp import EmailBackend

class UnsafeEmailBackend(EmailBackend):
    def open(self):
        # Override SSL context ili kupuuza verification
        self.ssl_context = ssl._create_unverified_context()
        return super().open()
