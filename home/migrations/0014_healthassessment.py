# Generated by Django 4.1.7 on 2023-04-13 00:58

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0013_remove_healthquestion_assessment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthAssessment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('instructions', models.CharField(max_length=500)),
                ('content', wagtail.fields.StreamField([('content', wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(form_classname='question'))]))], use_json_field=None)),
                ('logo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='health_assessment_logo', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
