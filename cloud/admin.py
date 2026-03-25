from django.contrib import admin
from django.utils.html import format_html
from .models import TestImage

@admin.register(TestImage)
class TestImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'uploaded_at', 'image_tag')
    readonly_fields = ('uploaded_at',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:80px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = 'Image Preview'
