from django.contrib import admin
from . models import *
# Register your models here.

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "image","is_active",)
    search_fields = ("name",)

class CourseFeacturesInline(admin.TabularInline):
    model = CourseFeactures
    extra = 1
    
class CourseDetailInline(admin.TabularInline):
    model = CourseDetail
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines=(CourseFeacturesInline,CourseDetailInline)
    list_display = ("title","image")
    search_fields = ("title",)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "image","is_active",)
    search_fields = ("title",)

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "address",)
    search_fields = ("name",)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number",)
    search_fields = ("name",)

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number",)
    search_fields = ("name",)

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = (GalleryImageInline,)
    list_display = ("name","order")

@admin.register(CourseOverview)
class CourseOverviewAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

@admin.register(Expert)
class CourseOverviewAdmin(admin.ModelAdmin):
    list_display = ("name","position","is_active",)
    search_fields = ("name",)