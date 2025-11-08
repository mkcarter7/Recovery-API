from django.db import models


class Partner(models.Model):
    """Community or organizational partner displayed on the site."""

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    website_url = models.URLField(blank=True)
    logo_url = models.URLField(blank=True)
    order = models.IntegerField(default=0, help_text="Display order on the site.")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
