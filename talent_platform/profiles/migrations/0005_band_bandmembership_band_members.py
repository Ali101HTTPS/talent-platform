# Generated by Django 5.1.6 on 2025-03-31 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_backgroundjobsprofile_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='band_profile_pictures/')),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_bands', to='profiles.talentuserprofile')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bands', to='profiles.genre')),
            ],
        ),
        migrations.CreateModel(
            name='BandMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('member', 'Member')], default='member', max_length=10)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.band')),
                ('talent_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.talentuserprofile')),
            ],
            options={
                'unique_together': {('talent_user', 'band')},
            },
        ),
        migrations.AddField(
            model_name='band',
            name='members',
            field=models.ManyToManyField(related_name='bands', through='profiles.BandMembership', to='profiles.talentuserprofile'),
        ),
    ]
