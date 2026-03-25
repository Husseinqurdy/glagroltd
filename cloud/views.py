from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User

from .models import (
    ConsultationOrder,
    ExpertConsultation,
    FarmManagementService, 
    FarmServiceOrder,
    FarmServiceReport,
    FarmerBlog,
    Fertilizer, 
    FertilizerOrder, 
    Seed,
    SeedOrder
)

from .serializers import (
    ConsultationOrderSerializer,
    ExpertConsultationSerializer,
    FarmManagementServiceSerializer, 
    FarmServiceOrderSerializer,
    FarmServiceReportSerializer,
    FarmerBlogSerializer,
    FertilizerSerializer, 
    FertilizerOrderSerializer, 
    SeedOrderSerializer, 
    SeedSerializer,
    LoginSerializer,
    SignupSerializer
)


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({
                "message": "Login successful",
                "username": user.username,
                "email": user.email
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FertilizerViewSet(viewsets.ModelViewSet):
    queryset = Fertilizer.objects.all()
    serializer_class = FertilizerSerializer


class FertilizerOrderViewSet(viewsets.ModelViewSet):
    queryset = FertilizerOrder.objects.all()
    serializer_class = FertilizerOrderSerializer


class SeedViewSet(viewsets.ModelViewSet):
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer



class SeedOrderViewSet(viewsets.ModelViewSet):
    queryset = SeedOrder.objects.all()
    serializer_class = SeedOrderSerializer


class FarmManagementServiceViewSet(viewsets.ModelViewSet):
    queryset = FarmManagementService.objects.all()
    serializer_class = FarmManagementServiceSerializer


class FarmServiceReportViewSet(viewsets.ModelViewSet):
    queryset = FarmServiceReport.objects.all()
    serializer_class = FarmServiceReportSerializer


class FarmServiceOrderViewSet(viewsets.ModelViewSet):
    queryset = FarmServiceOrder.objects.all()
    serializer_class = FarmServiceOrderSerializer



class ExpertConsultationViewSet(viewsets.ModelViewSet):
    queryset = ExpertConsultation.objects.all()
    serializer_class = ExpertConsultationSerializer


class ConsultationOrderViewSet(viewsets.ModelViewSet):
    queryset = ConsultationOrder.objects.all()
    serializer_class = ConsultationOrderSerializer



class FarmerBlogViewSet(viewsets.ModelViewSet):
    queryset = FarmerBlog.objects.all().order_by('-created_at')
    serializer_class = FarmerBlogSerializer
