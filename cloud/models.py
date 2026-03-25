from django.db import models
from cloudinary.models import CloudinaryField

class TestImage(models.Model):
    image = CloudinaryField('image')  # 🔥 muhimu sana
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"