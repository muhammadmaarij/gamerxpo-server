from rest_framework import serializers
from .models import Booth, Game, Theme, BoothCustomization, UserProfile, Organization, Conversation, ConversationMessage, GameFeedback, Event, Sponsorship
from django.contrib.auth.models import User


class BoothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booth
        fields = ['id', 'company', 'name',
                  'description', 'image', 'created_at']


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class BoothCustomizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoothCustomization
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['role', 'profile_picture', 'profile_picture_url']
        read_only_fields = ['user']


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'read_only': True},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username')


class MyUserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested serializer

    class Meta:
        model = UserProfile
        fields = ('user', 'profile_picture', 'profile_picture_url', 'role')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class ConversationListSerializer(serializers.ModelSerializer):
    users = UserDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ('id', 'users', 'modified_at',)


class ConversationDetailSerializer(serializers.ModelSerializer):
    users = UserDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ('id', 'users', 'modified_at',)


class ConversationMessageSerializer(serializers.ModelSerializer):
    sent_to = UserDetailSerializer(many=False, read_only=True)
    created_by = UserDetailSerializer(many=False, read_only=True)

    class Meta:
        model = ConversationMessage
        fields = ('id', 'body', 'sent_to', 'created_by', 'created_at')


class GameFeedbackSerializer(serializers.ModelSerializer):
    # User details are not editable
    submitted_by = UserSerializer(read_only=True)

    class Meta:
        model = GameFeedback
        fields = ['id', 'game', 'feedback_text', 'created_at', 'submitted_by']
        read_only_fields = ['created_at', 'submitted_by']

    def create(self, validated_data):
        # The user is added automatically in the view
        return super().create(validated_data)


class SponsorshipSerializer(serializers.ModelSerializer):
    # Ensure the logo is returned as a URL
    logo = serializers.ImageField(use_url=True)

    class Meta:
        model = Sponsorship
        fields = ['id', 'event', 'package', 'name', 'price', 'details', 'logo']
        # Set id as read-only if not already set by default
        read_only_fields = ['id']
