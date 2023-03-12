from django.contrib.auth.models import AbstractUser
from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image


class User(AbstractUser):
    mental_score = models.IntegerField(default=0)
    anxiety_score = models.IntegerField(default=0)
    depression_score = models.IntegerField(default=0)


class Activity(ClusterableModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=False, null=False)
    logo = models.ForeignKey(Image, blank=False, on_delete=models.CASCADE, related_name="activity_logo")
    photo = models.ForeignKey(Image, blank=False, on_delete=models.CASCADE, related_name="activity_photo")
    five_way_tag = models.CharField(max_length=50, blank=False)
    tags = models.CharField(max_length=300, blank=True)

    panel = [MultiFieldPanel([
        ImageChooserPanel("logo"),
        ImageChooserPanel("photo"),
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("five_way_tag"),
        FieldPanel("tags"),
    ])]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"


class Inspiration(ClusterableModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=False, null=False)
    photo = models.ForeignKey(Image, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class HealthAssessment(ClusterableModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    logo = models.ForeignKey(Image, blank=False, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, blank=False, null=False)
    num_questions = models.IntegerField()

    def __str__(self):
        return self.title


class MentalHealthResource(ClusterableModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    logo = models.ForeignKey(Image, blank=False, on_delete=models.CASCADE, related_name="mental_health_resource_logo")
    description = models.CharField(max_length=1000, blank=False, null=False)
    photo = models.ForeignKey(Image, blank=False, on_delete=models.CASCADE, related_name="mental_health_resource_photo")
    resource_type = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.title


class HealthQuestion(ClusterableModel):
    id = models.AutoField(primary_key=True)
    assessment = models.ForeignKey(HealthAssessment, blank=False, on_delete=models.CASCADE)
    question = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.question


class UserFavouriteActivity(ClusterableModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.activity


class UserAssessment(ClusterableModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    assessment = models.ForeignKey(HealthAssessment, on_delete=models.CASCADE)
    answers = models.CharField(max_length=500, blank=False, null=False)
    score = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class UserMood(ClusterableModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    mood = models.CharField(max_length=50)
    comment = models.CharField(max_length=500, blank=True, null=True)
    is_shared = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    tags = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.mood


class UserActivity(ClusterableModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey(Image, blank=True, null=True, on_delete=models.CASCADE)
    has_benefit = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=False)
    comment = models.CharField(max_length=500, blank=True, null=True)
    isShared = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.activity


class UserSelfReflection(ClusterableModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=False, null=False)
    mood = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey(Image, blank=True, null=True, on_delete=models.CASCADE)
    isShared = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user
