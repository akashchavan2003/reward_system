# Generated by Django 4.1.13 on 2024-08-28 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_app', '0002_usertask_remove_userprofile_user_delete_task_and_more'),
        ('admin_app', '0002_admintask'),
    ]

    operations = [
        migrations.DeleteModel(
            name='App',
        ),
        migrations.AddField(
            model_name='admintask',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
