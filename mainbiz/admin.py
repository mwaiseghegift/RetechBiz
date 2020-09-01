from django.contrib import admin
from .models import (Service, Gallery, 
                    About, AboutUsService, Testimonial,
                    Sponsor, Intro, Blog, Category, Comment)
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ['name', 'description', 'image']

admin.site.register(Service, ServiceAdmin)

class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ['name','description','image']

    class Meta:
        verbose_name_plural = 'Galleries'

admin.site.register(Gallery, GalleryAdmin)

#AboutUs

class AboutUsServiceInline(admin.TabularInline):
    model = AboutUsService
    extra = 3

class AboutAdmin(admin.ModelAdmin):
    inlines = [AboutUsServiceInline]
    list_display = ['title','description','image']


admin.site.register(About, AboutAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['user','pub_date', 'image','text',]
    
admin.site.register(Testimonial, TestimonialAdmin)

class SponsorAdmin(admin.ModelAdmin):
    list_display = ['name','logo']

admin.site.register(Sponsor, SponsorAdmin)

class IntroAdmin(admin.ModelAdmin):
    list_display = ['name','text']

admin.site.register(Intro, IntroAdmin)

###########################################

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['title','author','pub_date','updated_on']
    list_filter = ['pub_date','updated_on']
    search_fields = ['title','author']

admin.site.register(Blog, BlogAdmin)

#############################################

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

    class Meta:
        verbose_name_plural = 'Categories'

admin.site.register(Category, CategoryAdmin)