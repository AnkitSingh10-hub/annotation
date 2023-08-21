# Generated by Django 4.1.3 on 2023-08-21 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plantrecognitionapp', '0007_annotation_json_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='color',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='height',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='width',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='x',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='y',
        ),
        migrations.AddField(
            model_name='annotation',
            name='plant_images',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='plantrecognitionapp.plantimage'),
            preserve_default=False,
        ),
    ]
