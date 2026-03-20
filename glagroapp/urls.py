from rest_framework.routers import DefaultRouter
from .views import (
    ConsultationOrderViewSet,
    ExpertConsultationViewSet,
    FarmManagementServiceViewSet,
    FarmServiceOrderViewSet, 
    FarmServiceReportViewSet, 
    FertilizerViewSet, 
    FertilizerOrderViewSet, 
    SeedOrderViewSet, 
    SeedViewSet
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

urlpatterns = router.urls

