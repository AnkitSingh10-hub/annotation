# Generated by Django 4.1.3 on 2023-08-20 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantrecognitionapp', '0004_remove_annotation_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='height',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='width',
        ),
    ]