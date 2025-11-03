from django.contrib import admin
from .models import Program, Testimonial, ContactSubmission, NewsletterSubscriber, Feature, SiteContent


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'program_type', 'is_active', 'order']
    list_filter = ['program_type', 'is_active']
    search_fields = ['name', 'description']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_name', 'is_featured', 'is_active', 'order']
    list_filter = ['is_featured', 'is_active']
    search_fields = ['title', 'content', 'author_name']


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at']


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'subscribed_at']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['email', 'first_name', 'last_name']
    readonly_fields = ['subscribed_at', 'unsubscribed_at']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'description']


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ['content_type', 'updated_at']
    readonly_fields = ['updated_at']
