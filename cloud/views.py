from rest_framework import viewsets
from .models import TestImage
from .serializers import TestImageSerializer

class TestImageViewSet(viewsets.ModelViewSet):
    queryset = TestImage.objects.all().order_by('-uploaded_at')
    serializer_class = TestImageSerializer
