# Generated by Django 5.1.6 on 2025-05-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_restrictedcountryuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restrictedcountryuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
