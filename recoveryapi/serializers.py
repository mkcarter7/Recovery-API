from rest_framework import serializers
from .models import (
    Program,
    ProgramType,
    Testimonial,
    ContactSubmission,
    NewsletterSubscriber,
    Feature,
    SiteContent,
    TeamMember,
    Partner,
)


class ProgramSerializer(serializers.ModelSerializer):
    """Serializer for Program model"""
    program_type = serializers.SlugRelatedField(
        slug_field='code',
        queryset=ProgramType.objects.all()
    )
    program_type_name = serializers.CharField(source='program_type.name', read_only=True)
    program_type_detail = serializers.SerializerMethodField()

    class Meta:
        model = Program
        fields = [
            'id',
            'name',
            'slug',
            'program_type',
            'program_type_name',
            'program_type_detail',
            'description',
            'short_description',
            'features',
            'is_active',
            'order',
            'created_at',
            'updated_at',
        ]

    def get_program_type_detail(self, obj):
        return ProgramTypeSerializer(obj.program_type).data


class ProgramTypeSerializer(serializers.ModelSerializer):
    """Serializer for ProgramType model."""

    class Meta:
        model = ProgramType
        fields = ['id', 'code', 'name', 'description', 'order', 'is_active']


class TeamMemberSerializer(serializers.ModelSerializer):
    """Serializer for TeamMember model."""

    class Meta:
        model = TeamMember
        fields = [
            'id',
            'name',
            'role',
            'bio',
            'photo_url',
            'email',
            'linkedin_url',
            'order',
            'is_active',
            'created_at',
            'updated_at',
        ]


class PartnerSerializer(serializers.ModelSerializer):
    """Serializer for Partner model."""

    class Meta:
        model = Partner
        fields = [
            'id',
            'name',
            'description',
            'website_url',
            'logo_url',
            'order',
            'is_active',
            'created_at',
            'updated_at',
        ]


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
