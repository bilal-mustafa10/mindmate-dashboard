from rest_framework import serializers

from home.models import Activity, Inspiration, HealthAssessment, MentalHealthResource, HealthQuestion, User


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


class HealthAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthAssessment
        fields = '__all__'


class HealthQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthQuestion
        fields = '__all__'
