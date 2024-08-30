from django.db import models
from django.contrib.auth.models import User

class AdminTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_tasks')
    app_name = models.CharField(max_length=255)
    task_description = models.TextField()
    points = models.IntegerField(default=0)
    link = models.URLField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return f"{self.app_name} for {self.user.username}"