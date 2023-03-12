# Generated by Django 4.1.7 on 2023-03-11 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0002_activity_healthassessment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'Activity', 'verbose_name_plural': 'Activities'},
        ),
        migrations.CreateModel(
            name='MentalHealthResource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('resource_type', models.CharField(max_length=50)),
                ('logo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mental_health_resource_logo', to='wagtailimages.image')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mental_health_resource_photo', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
