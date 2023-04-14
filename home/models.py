from django.contrib.auth.models import AbstractUser
from django.db import models, transaction
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.core import blocks


class User(AbstractUser):
    mental_score = models.IntegerField(default=0)
    anxiety_score = models.IntegerField(default=0)
    depression_score = models.IntegerField(default=0)


class Activity(ClusterableModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = RichTextField(max_length=3600, verbose_name="Activity Description", blank=False, null=True,
                                features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'image',
                                          'document-link', 'embed'])
    logo = models.ForeignKey(Image, blank=False, on_delete=models.CASCADE, related_name="activity_logo")
    photo = models.ForeignKey(Image, blank=False, on_delete=models.CASCADE, related_name="activity_photo")
    five_way_tag = models.CharField(max_length=50, blank=False)
    tags = models.CharField(max_length=300, blank=True)

    panel = [MultiFieldPanel([
        FieldPanel("logo"),
        FieldPanel("photo"),
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


class MentalHealthResource(ClusterableModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    logo = models.ForeignKey(Image, blank=False, on_delete=models.CASCADE, related_name="mental_health_resource_logo")
    content = StreamField([
        ('content', blocks.StructBlock(
            [('title', blocks.CharBlock(form_classname="Title")),
             ('description', blocks.RichTextBlock(form_classname="Description")), ]))
    ])
    daily_boost = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class HealthAssessment(ClusterableModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    logo = models.ForeignKey(Image, blank=False, on_delete=models.CASCADE, related_name="health_assessment_logo")
    instructions = RichTextField(max_length=3600, verbose_name="Instructions", blank=False, null=True,
                                features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'link', 'image',
                                          'document-link', 'embed'])
    content = StreamField([
        ('content', blocks.StructBlock(
            [('question', blocks.CharBlock(form_classname="question")),

    ]))])


class UserHub(ClusterableModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="user_hub_user")
    type = models.CharField(max_length=50, blank=False, null=False)
    datetime = models.DateTimeField(blank=False, null=False)
    likes = models.ManyToManyField(User, blank=True, null=True, related_name="user_hub_likes")
    activity_id = models.IntegerField(blank=True, null=True)  ## activity
    photos = models.ManyToManyField(Image, blank=True, null=True, related_name="user_hub_photos") ## activity
    mood = models.CharField(max_length=50, blank=True, null=True) ## mood
    notes = models.TextField(blank=True, null=True) ## mood / reflection
    title = models.CharField(max_length=50, blank=True, null=True) ## reflection

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            for photo in self.photos.all():
                photo.delete()

            self.photos.clear()
            self.likes.clear()
            super(UserHub, self).delete(*args, **kwargs)


    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "User Hub"
        verbose_name_plural = "User Hub"
