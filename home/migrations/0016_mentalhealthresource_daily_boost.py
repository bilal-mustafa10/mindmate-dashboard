# Generated by Django 4.1.7 on 2023-04-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_healthassessment_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentalhealthresource',
            name='daily_boost',
            field=models.BooleanField(default=False),
        ),
    ]
