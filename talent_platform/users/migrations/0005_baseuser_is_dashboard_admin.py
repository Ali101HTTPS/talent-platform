# Generated by Django 5.1.6 on 2025-05-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_baseuser_stripe_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='is_dashboard_admin',
            field=models.BooleanField(default=False),
        ),
    ]
