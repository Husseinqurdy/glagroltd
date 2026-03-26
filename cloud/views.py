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
    ForgotPasswordSerializer,
    ResetPasswordSerializer, 
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
    


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                "message": "Reset token generated",
                "reset_token": serializer.validated_data['reset_token']
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            new_password = serializer.validated_data['new_password']

            # Demo: tafuta user kwa token (kwa sasa tunatumia email au token ya demo)
            # Production: hifadhi token kwenye DB na uhusishe na user
            user = User.objects.filter(email="user@example.com").first()  # mfano tu

            if user:
                user.set_password(new_password)  # hashing sahihi
                user.save()
                return Response({"message": "Password reset successful"}, status=status.HTTP_200_OK)

            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

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
