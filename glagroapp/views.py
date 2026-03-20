from rest_framework import viewsets
from .models import (
    ConsultationOrder,
    ExpertConsultation,
    FarmManagementService, 
    FarmServiceOrder,
    FarmServiceReport,
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
    FertilizerSerializer, 
    FertilizerOrderSerializer, 
    SeedOrderSerializer, 
    SeedSerializer
)

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
