# Generated by Django 4.1.3 on 2023-08-21 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantrecognitionapp', '0006_annotation_height_annotation_width'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='json_data',
            field=models.JSONField(null=True),
        ),
    ]