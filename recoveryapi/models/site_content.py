from django.db import models


class SiteContent(models.Model):
    """General site content/configuration"""
    CONTENT_TYPES = [
        ('hero_title', 'Hero Title'),
        ('hero_subtitle', 'Hero Subtitle'),
        ('about_story', 'About Story'),
        ('about_mission', 'About Mission'),
        ('contact_phone', 'Contact Phone'),
    ]

    content_type = models.CharField(max_length=50, choices=CONTENT_TYPES, unique=True)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content_type
