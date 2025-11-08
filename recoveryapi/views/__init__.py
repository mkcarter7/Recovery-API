"""
Recovery API Views Package

This package contains all the ViewSets for the Recovery API application.
Each ViewSet handles CRUD operations and custom actions for their respective models.
"""

from .program import (
    ProgramViewSet,
    ProgramAdminViewSet,
    ProgramTypeViewSet,
    ProgramTypeAdminViewSet,
)
from .testimonial import TestimonialViewSet
from .contact import ContactSubmissionView, ContactSubmissionAdminViewSet
from .newsletter import NewsletterSubscriberView, NewsletterSubscriberAdminViewSet
from .feature import FeatureViewSet
from .site_content import SiteContentViewSet, SiteContentAdminViewSet
from .team import TeamMemberViewSet, TeamMemberAdminViewSet
from .partner import PartnerViewSet, PartnerAdminViewSet

__all__ = [
    'ProgramViewSet',
    'ProgramAdminViewSet',
    'ProgramTypeViewSet',
    'ProgramTypeAdminViewSet',
    'TestimonialViewSet',
    'ContactSubmissionView',
    'ContactSubmissionAdminViewSet',
    'NewsletterSubscriberView',
    'NewsletterSubscriberAdminViewSet',
    'FeatureViewSet',
    'SiteContentViewSet',
    'SiteContentAdminViewSet',
    'TeamMemberViewSet',
    'TeamMemberAdminViewSet',
    'PartnerViewSet',
    'PartnerAdminViewSet',
]
