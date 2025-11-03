from rest_framework import serializers
from .models import Program, Testimonial, ContactSubmission, NewsletterSubscriber, Feature, SiteContent


class ProgramSerializer(serializers.ModelSerializer):
    """Serializer for Program model"""
    class Meta:
        model = Program
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    """Serializer for Testimonial model"""
    class Meta:
        model = Testimonial
        fields = '__all__'


class ContactSubmissionSerializer(serializers.ModelSerializer):
    """Serializer for ContactSubmission model"""
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'phone', 'message']
        read_only_fields = ['is_read', 'created_at']

    def create(self, validated_data):
        return ContactSubmission.objects.create(**validated_data)


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    """Serializer for NewsletterSubscriber model"""
    class Meta:
        model = NewsletterSubscriber
        fields = ['first_name', 'last_name', 'email']
        read_only_fields = ['is_active', 'subscribed_at']

    def create(self, validated_data):
        # If email already exists, reactivate it
        email = validated_data.get('email')
        subscriber, created = NewsletterSubscriber.objects.get_or_create(
            email=email,
            defaults=validated_data
        )
        if not created:
            subscriber.is_active = True
            subscriber.first_name = validated_data.get('first_name', subscriber.first_name)
            subscriber.last_name = validated_data.get('last_name', subscriber.last_name)
            subscriber.unsubscribed_at = None
            subscriber.save()
        return subscriber


class FeatureSerializer(serializers.ModelSerializer):
    """Serializer for Feature model"""
    class Meta:
        model = Feature
        fields = '__all__'


class SiteContentSerializer(serializers.ModelSerializer):
    """Serializer for SiteContent model"""
    class Meta:
        model = SiteContent
        fields = '__all__'


class ContactSubmissionAdminSerializer(serializers.ModelSerializer):
    """Admin serializer for ContactSubmission with all fields"""
    class Meta:
        model = ContactSubmission
        fields = ['id', 'name', 'email', 'phone', 'message', 'is_read', 'created_at']
        read_only_fields = ['id', 'created_at']


class NewsletterSubscriberAdminSerializer(serializers.ModelSerializer):
    """Admin serializer for NewsletterSubscriber with all fields"""
    class Meta:
        model = NewsletterSubscriber
        fields = ['id', 'first_name', 'last_name', 'email', 'is_active', 'subscribed_at', 'unsubscribed_at']
        read_only_fields = ['id', 'subscribed_at']
