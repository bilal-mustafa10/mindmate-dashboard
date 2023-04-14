from rest_framework import serializers
from wagtail.images.models import Image

from home.models import Activity, Inspiration, MentalHealthResource, User, UserHub, HealthAssessment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        depth = 1


class InspirationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspiration
        fields = '__all__'


class MentalHealthResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalHealthResource
        fields = '__all__'
        depth = 1


class HealthAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthAssessment
        fields = '__all__'
        depth = 1

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class UserHubSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    likes = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False)
    photos = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all(), many=True, required=False)

    class Meta:
        model = UserHub
        fields = [
            'id',
            'user',
            'type',
            'datetime',
            'likes',
            'activity_id',
            'photos',
            'mood',
            'notes',
            'title'
        ]

    def to_representation(self, instance):
        self.fields['photos'] = ImageSerializer(many=True)
        return super(UserHubSerializer, self).to_representation(instance)