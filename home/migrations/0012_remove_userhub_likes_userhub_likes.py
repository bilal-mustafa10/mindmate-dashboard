# Generated by Django 4.1.7 on 2023-04-10 05:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_userhub_likes_alter_userhub_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userhub',
            name='likes',
        ),
        migrations.AddField(
            model_name='userhub',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_hub_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]