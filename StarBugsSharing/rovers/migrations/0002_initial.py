# Generated by Django 4.2.7 on 2024-01-20 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rovers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='using',
            name='user',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='usings', to=settings.AUTH_USER_MODEL),
        ),
    ]
