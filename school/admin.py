from django.contrib import admin
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from .models import (
    SchoolConfig, 
    HeroSlider, 
    Facility, 
    Notice, 
    Event, 
    GalleryCategory, 
    GalleryImage, 
    Teacher, 
    ContactQuery
)

@admin.register(SchoolConfig)
class SchoolConfigAdmin(admin.ModelAdmin):
    # Prevent adding new configurations once one exists
    def has_add_permission(self, request):
        if SchoolConfig.objects.exists():
            return False
        return True

    # Prevent deleting the configuration
    def has_delete_permission(self, request, obj=None):
        return False

    # Redirect the main configuration list directly to the edit page of the singleton
    def changelist_view(self, request, extra_context=None):
        obj = SchoolConfig.get_solo()
        return redirect('admin:school_schoolconfig_change', obj.pk)


@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'image_preview')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'subtitle')
    
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px; border-radius: 4px;" />')
        return "No Image"
    image_preview.short_description = 'Preview'


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_name', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_urgent', 'is_active', 'created_at')
    list_editable = ('is_urgent', 'is_active')
    list_filter = ('is_urgent', 'is_active', 'created_at')
    search_fields = ('title', 'content')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'image_preview')
    list_filter = ('date',)
    search_fields = ('title', 'description', 'location')

    def image_preview(self, obj):
        if obj.thumbnail:
            return mark_safe(f'<img src="{obj.thumbnail.url}" style="max-height: 50px; border-radius: 4px;" />')
        return "No Image"
    image_preview.short_description = 'Thumbnail'


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'category', 'order', 'image_preview')
    list_filter = ('category',)
    list_editable = ('order',)
    search_fields = ('caption',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px; border-radius: 4px;" />')
        return "No Image"
    image_preview.short_description = 'Image'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'qualification', 'order', 'image_preview')
    list_editable = ('order',)
    search_fields = ('name', 'designation', 'qualification')

    def image_preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 50px; width: 50px; border-radius: 50%; object-fit: cover;" />')
        return "No Photo"
    image_preview.short_description = 'Photo'


@admin.register(ContactQuery)
class ContactQueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'phone', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    list_editable = ('is_read',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'created_at')
