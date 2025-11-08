from django.db import models
from django.utils.text import slugify


class ProgramType(models.Model):
    """Program category that can be managed via the admin."""

    code = models.CharField(
        max_length=50,
        unique=True,
        help_text="Short identifier used by the frontend (e.g. 'IOP').",
    )
    name = models.CharField(max_length=200, help_text="Human-friendly name.")
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0, help_text="Display order.")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.code})" if self.name else self.code


class Program(models.Model):
    """Recovery program model"""

    name = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=120,
        unique=True,
        help_text="URL-friendly slug used on the client application.",
    )
    program_type = models.ForeignKey(
        ProgramType,
        on_delete=models.PROTECT,
        related_name='programs',
    )
    description = models.TextField()
    short_description = models.TextField(blank=True, help_text="Brief description for homepage")
    features = models.JSONField(default=list, help_text="List of program features")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
