# Generated by Django 5.1.6 on 2025-04-24 11:52

import django.db.models.deletion
import profiles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_remove_band_genre_band_band_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundjobsprofile',
            name='account_type',
            field=models.CharField(choices=[('back_ground_jobs', 'Background Jobs'), ('free', 'Free')], default='free', max_length=20),
        ),
        migrations.CreateModel(
            name='BandMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled Media', max_length=124)),
                ('media_info', models.TextField(max_length=160)),
                ('media_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video')], max_length=10)),
                ('media_file', models.FileField(upload_to=profiles.models.band_media_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='profiles.band')),
            ],
        ),
    ]
