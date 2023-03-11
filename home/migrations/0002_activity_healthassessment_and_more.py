# Generated by Django 4.1.7 on 2023-03-10 23:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('five_way_tag', models.CharField(max_length=50)),
                ('tags', models.CharField(blank=True, max_length=300)),
                ('logo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_logo', to='wagtailimages.image')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_photo', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HealthAssessment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('num_questions', models.IntegerField()),
                ('logo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='user',
            old_name='anxietyScore',
            new_name='anxiety_score',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='depressionScore',
            new_name='depression_score',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='mentalScore',
            new_name='mental_score',
        ),
        migrations.CreateModel(
            name='UserSelfReflection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('mood', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('isShared', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wagtailimages.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserMood',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mood', models.CharField(max_length=50)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('is_shared', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('tags', models.CharField(blank=True, max_length=300, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserFavouriteActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAssessment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('answers', models.CharField(max_length=500)),
                ('score', models.IntegerField()),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.healthassessment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('has_benefit', models.BooleanField(default=False)),
                ('is_recommended', models.BooleanField(default=False)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('isShared', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.activity')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wagtailimages.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Inspiration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HealthQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.healthassessment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
