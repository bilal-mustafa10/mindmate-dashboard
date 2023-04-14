from rest_framework import viewsets
from wagtail.images.models import Image

from home.models import Activity, Inspiration, MentalHealthResource, User, UserHub, HealthAssessment
from home.serializers import ActivitySerializer, InspirationSerializer, \
    MentalHealthResourceSerializer, UserSerializer, UserHubSerializer, ImageSerializer, HealthAssessmentSerializer


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

class UserHubViewSet(viewsets.ModelViewSet):
    queryset = UserHub.objects.all()
    serializer_class = UserHubSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
