from django.db import models


class Program(models.Model):
    """Recovery program model"""
    PROGRAM_TYPES = [
        ('PHP', 'Partial Hospitalization Program'),
        ('IOP', 'Intensive Outpatient Program'),
        ('VOC', 'Vocational Rehabilitation'),
        ('RES', 'Respite Housing'),
    ]

    name = models.CharField(max_length=200)
    program_type = models.CharField(max_length=3, choices=PROGRAM_TYPES)
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
