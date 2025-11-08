from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from recoveryapi.views import (
    ProgramTypeViewSet,
    ProgramTypeAdminViewSet,
    ProgramViewSet,
    ProgramAdminViewSet,
    TeamMemberViewSet,
    TeamMemberAdminViewSet,
    PartnerViewSet,
    PartnerAdminViewSet,
    TestimonialViewSet,
    ContactSubmissionView,
    NewsletterSubscriberView,
    FeatureViewSet,
    SiteContentViewSet,
    SiteContentAdminViewSet,
    ContactSubmissionAdminViewSet,
    NewsletterSubscriberAdminViewSet,
)

router = DefaultRouter()
router.register(r'program-types', ProgramTypeViewSet, basename='program-type')
router.register(r'programs', ProgramViewSet, basename='program')
router.register(r'team-members', TeamMemberViewSet, basename='team-member')
router.register(r'partners', PartnerViewSet, basename='partner')
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')
router.register(r'features', FeatureViewSet, basename='feature')
router.register(r'site-content', SiteContentViewSet, basename='site-content')

admin_router = DefaultRouter()
admin_router.register(r'program-types', ProgramTypeAdminViewSet, basename='admin-program-types')
admin_router.register(r'programs', ProgramAdminViewSet, basename='admin-programs')
admin_router.register(r'team-members', TeamMemberAdminViewSet, basename='admin-team-members')
admin_router.register(r'partners', PartnerAdminViewSet, basename='admin-partners')
admin_router.register(r'site-content', SiteContentAdminViewSet, basename='admin-site-content')
admin_router.register(r'contact-submissions', ContactSubmissionAdminViewSet, basename='admin-contact-submissions')
admin_router.register(r'newsletter-subscriptions', NewsletterSubscriberAdminViewSet, basename='admin-newsletter-subscriptions')

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=False), name='index'),
    path('api/', include(router.urls)),
    path('api/contact/', ContactSubmissionView.as_view(), name='contact'),
    path('api/newsletter/', NewsletterSubscriberView.as_view(), name='newsletter'),
    path('api/admin/', include(admin_router.urls)),
    path('admin/', admin.site.urls),
]
