from django.db import models
from django.contrib.auth.models import User
import admin_app.models


class UserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tasks')
    admin_task = models.ForeignKey(admin_app.models.AdminTask, on_delete=models.CASCADE, related_name='user_tasks')
    screenshot = models.ImageField(upload_to='screenshots/', null=True, blank=True)
    points = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.user.username} - {self.admin_task.app_name}"
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=0)
    points_earned = models.IntegerField(default=0)
    task_completed=models.IntegerField(default=0)

