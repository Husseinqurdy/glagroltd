from rest_framework import serializers
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

class FertilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fertilizer
        fields = '__all__'


class FertilizerOrderSerializer(serializers.ModelSerializer):
    fertilizer_name = serializers.CharField(source="fertilizer.name", read_only=True)

    class Meta:
        model = FertilizerOrder
        fields = '__all__'



class SeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seed
        fields = '__all__'   



class SeedOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeedOrder
        fields = '__all__'
        read_only_fields = ['created_at']



class FarmManagementServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmManagementService
        fields = '__all__'


class FarmServiceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmServiceReport
        fields = '__all__'
        read_only_fields = ['created_at']


class FarmServiceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmServiceOrder
        fields = '__all__'
        read_only_fields = ['created_at']




class ExpertConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertConsultation
        fields = '__all__'


class ConsultationOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationOrder
        fields = '__all__'
        read_only_fields = ['created_at']



class FarmerBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerBlog
        fields = '__all__'
