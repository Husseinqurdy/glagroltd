from django.contrib import admin
from .models import ConsultationOrder, ExpertConsultation, FarmManagementService, FarmServiceOrder, FarmServiceReport, Fertilizer, FertilizerOrder, Seed, SeedOrder

@admin.register(Fertilizer)
class FertilizerAdmin(admin.ModelAdmin):
    list_display = ('name_sw', 'name_en', 'price', 'created_at')
    search_fields = ('name_sw', 'name_en')

@admin.register(FertilizerOrder)
class FertilizerOrderAdmin(admin.ModelAdmin):
    list_display = ('fertilizer', 'customer_name', 'phone_number', 'quantity', 'location', 'created_at')
    search_fields = ('customer_name', 'phone_number')

@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
    list_display = ('name_sw', 'name_en', 'price', 'created_at')
    search_fields = ('name_sw', 'name_en')

@admin.register(SeedOrder)
class SeedOrderAdmin(admin.ModelAdmin):
    list_display = ('seed', 'customer_name', 'customer_phone', 'location', 'created_at')
    search_fields = ('customer_name', 'customer_phone')
    

@admin.register(FarmManagementService)
class FarmManagementServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name_sw', 'service_name_en', 'created_at', 'updated_at')
    search_fields = ('service_name_sw', 'service_name_en')
    list_filter = ('created_at', 'updated_at')


@admin.register(FarmServiceReport)
class FarmServiceReportAdmin(admin.ModelAdmin):
    list_display = ('farmer_name', 'farmer_phone', 'location', 'service', 'created_at')
    search_fields = ('farmer_name', 'farmer_phone', 'location')
    list_filter = ('created_at', 'service')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Taarifa za Mkulima', {
            'fields': ('service', 'farmer_name', 'farmer_phone', 'location')
        }),
        ('Kabla ya Usimamizi', {
            'fields': ('before_description', 'before_image')
        }),
        ('Baada ya Usimamizi', {
            'fields': ('after_description', 'after_image')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )
    
  
@admin.register(FarmServiceOrder)
class FarmServiceOrderAdmin(admin.ModelAdmin):
    list_display = ('farmer_name', 'farmer_phone', 'location', 'service', 'created_at')
    search_fields = ('farmer_name', 'farmer_phone', 'location')
    list_filter = ('service', 'created_at')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Taarifa za Mkulima', {
            'fields': ('service', 'farmer_name', 'farmer_phone', 'location')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )



@admin.register(ExpertConsultation)
class ExpertConsultationAdmin(admin.ModelAdmin):
    list_display = ('topic_sw', 'topic_en', 'created_at', 'updated_at')
    search_fields = ('topic_sw', 'topic_en')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Mada ya Ushauri', {
            'fields': ('topic_sw', 'topic_en', 'description_sw', 'description_en', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(ConsultationOrder)
class ConsultationOrderAdmin(admin.ModelAdmin):
    list_display = ('farmer_name', 'farmer_phone', 'location', 'consultation', 'created_at')
    search_fields = ('farmer_name', 'farmer_phone', 'location', 'question')
    list_filter = ('consultation', 'created_at')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Taarifa za Mkulima', {
            'fields': ('consultation', 'farmer_name', 'farmer_phone', 'location')
        }),
        ('Swali la Ushauri', {
            'fields': ('question',)
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )

