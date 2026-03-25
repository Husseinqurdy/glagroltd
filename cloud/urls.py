from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    ConsultationOrderViewSet,
    ExpertConsultationViewSet,
    FarmManagementServiceViewSet,
    FarmServiceOrderViewSet, 
    FarmServiceReportViewSet,
    FarmerBlogViewSet, 
    FertilizerViewSet, 
    FertilizerOrderViewSet,
    LoginView, 
    SeedOrderViewSet, 
    SeedViewSet,
    SignupView
)


router = DefaultRouter()
router.register(r'fertilizers', FertilizerViewSet)
router.register(r'orders', FertilizerOrderViewSet)
router.register(r'seeds', SeedViewSet)
router.register(r'seed-orders', SeedOrderViewSet)
router.register(r'farm-services', FarmManagementServiceViewSet)
router.register(r'farm-service-reports', FarmServiceReportViewSet)
router.register(r'farm-service-orders', FarmServiceOrderViewSet)
router.register(r'expert-consultations', ExpertConsultationViewSet)
router.register(r'consultation-orders', ConsultationOrderViewSet)
router.register(r'farmer-blogs', FarmerBlogViewSet, basename='farmerblog')

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),


]
