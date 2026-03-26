from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
import uuid


from .models import (
    ConsultationOrder,
    ExpertConsultation,
    FarmManagementService,
    FarmServiceOrder, 
    FarmServiceReport,
    FarmerBlog,
    Fertilizer, 
    FertilizerOrder,
    PasswordResetToken, 
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


class SignupSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    username = serializers.CharField() 

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user




class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
       
        user_obj = User.objects.filter(email=data['email']).first()
        if not user_obj:
            raise serializers.ValidationError("Invalid email or password")

       
        user = authenticate(username=user_obj.username, password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid email or password")

        data['user'] = user
        return data



class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        user = User.objects.filter(email=data['email']).first()
        if not user:
            raise serializers.ValidationError("No account found with this email")
        token = str(uuid.uuid4())
        PasswordResetToken.objects.create(user=user, token=token)
        data['reset_token'] = token
        return data




class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        # Kwa sasa tunakubali token yoyote (demo). Production: hifadhi token kwenye DB.
        return data
