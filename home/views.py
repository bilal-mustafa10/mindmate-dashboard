from rest_framework import viewsets

from home.models import Activity, Inspiration, HealthAssessment, MentalHealthResource, User
from home.serializers import ActivitySerializer, InspirationSerializer, HealthAssessmentSerializer, \
    MentalHealthResourceSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class InspirationViewSet(viewsets.ModelViewSet):
    queryset = Inspiration.objects.all()
    serializer_class = InspirationSerializer


class MentalHealthResourceViewSet(viewsets.ModelViewSet):
    queryset = MentalHealthResource.objects.all()
    serializer_class = MentalHealthResourceSerializer


class HealthAssessmentViewSet(viewsets.ModelViewSet):
    queryset = HealthAssessment.objects.all()
    serializer_class = HealthAssessmentSerializer
