from django.contrib import admin
from django.utils.html import format_html
from .models import (
    ConsultationOrder, ExpertConsultation, FarmManagementService,
    FarmServiceOrder, FarmServiceReport, Fertilizer, FertilizerOrder,
    Seed, SeedOrder, FarmerBlog
)

@admin.register(Fertilizer)
class FertilizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'image_tag')
    search_fields = ('name',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'


@admin.register(FertilizerOrder)
class FertilizerOrderAdmin(admin.ModelAdmin):
    list_display = ('fertilizer', 'customer_name', 'phone_number', 'quantity', 'location', 'created_at')
    search_fields = ('customer_name', 'phone_number')


@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'image_tag')
    search_fields = ('name',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'


@admin.register(SeedOrder)
class SeedOrderAdmin(admin.ModelAdmin):
    list_display = ('seed', 'customer_name', 'customer_phone', 'location', 'created_at')
    search_fields = ('customer_name', 'customer_phone')


@admin.register(FarmManagementService)
class FarmManagementServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'created_at', 'updated_at', 'image_tag')
    search_fields = ('service_name',)
    list_filter = ('created_at', 'updated_at')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'


@admin.register(FarmServiceReport)
class FarmServiceReportAdmin(admin.ModelAdmin):
    list_display = ('farmer_name', 'farmer_phone', 'location', 'service', 'created_at', 'before_image_tag', 'after_image_tag')
    search_fields = ('farmer_name', 'farmer_phone', 'location')
    list_filter = ('created_at', 'service')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Farmer Information', {
            'fields': ('service', 'farmer_name', 'farmer_phone', 'location')
        }),
        ('Before Management', {
            'fields': ('before_description', 'before_image')
        }),
        ('After Management', {
            'fields': ('after_description', 'after_image')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )

    def before_image_tag(self, obj):
        if obj.before_image:
            return format_html('<img src="{}" style="height:50px;"/>', obj.before_image.url)
        return "-"
    before_image_tag.short_description = 'Before Image'

    def after_image_tag(self, obj):
        if obj.after_image:
            return format_html('<img src="{}" style="height:50px;"/>', obj.after_image.url)
        return "-"
    after_image_tag.short_description = 'After Image'


@admin.register(FarmServiceOrder)
class FarmServiceOrderAdmin(admin.ModelAdmin):
    list_display = ('farmer_name', 'farmer_phone', 'location', 'service', 'created_at')
    search_fields = ('farmer_name', 'farmer_phone', 'location')
    list_filter = ('service', 'created_at')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Farmer Information', {
            'fields': ('service', 'farmer_name', 'farmer_phone', 'location')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )


@admin.register(ExpertConsultation)
class ExpertConsultationAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created_at', 'updated_at', 'image_tag')
    search_fields = ('topic',)
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Consultation Topic', {
            'fields': ('topic', 'description', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'


@admin.register(ConsultationOrder)
class ConsultationOrderAdmin(admin.ModelAdmin):
    list_display = ('farmer_name', 'farmer_phone', 'location', 'consultation', 'created_at')
    search_fields = ('farmer_name', 'farmer_phone', 'location', 'question')
    list_filter = ('consultation', 'created_at')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Farmer Information', {
            'fields': ('consultation', 'farmer_name', 'farmer_phone', 'location')
        }),
        ('Consultation Question', {
            'fields': ('question',)
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )


@admin.register(FarmerBlog)
class FarmerBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'image_tag')
    search_fields = ('title', 'author')
    list_filter = ('created_at', 'updated_at')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'
