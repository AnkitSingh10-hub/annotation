# Generated by Django 4.1.3 on 2023-08-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantrecognitionapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='color',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
