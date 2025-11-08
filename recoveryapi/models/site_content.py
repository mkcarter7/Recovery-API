from django.db import models


class SiteContent(models.Model):
    """Key/value site content entries editable via the admin dashboard."""

    content_type = models.CharField(
        max_length=100,
        unique=True,
        help_text="Machine-friendly key (e.g. 'hero_headline', 'contact_phone').",
    )
    content = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content_type
