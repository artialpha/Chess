# Generated by Django 2.2.5 on 2019-10-18 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerrate',
            old_name='opening',
            new_name='player',
        ),
        migrations.AddField(
            model_name='playerrate',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]