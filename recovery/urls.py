from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from recoveryapi.views import (
    ProgramViewSet, TestimonialViewSet, ContactSubmissionView,
    NewsletterSubscriberView, FeatureViewSet, SiteContentViewSet
)

router = DefaultRouter()
router.register(r'programs', ProgramViewSet, basename='program')
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')
router.register(r'features', FeatureViewSet, basename='feature')
router.register(r'site-content', SiteContentViewSet, basename='site-content')

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=False), name='index'),
    path('api/', include(router.urls)),
    path('api/contact/', ContactSubmissionView.as_view(), name='contact'),
    path('api/newsletter/', NewsletterSubscriberView.as_view(), name='newsletter'),
]
