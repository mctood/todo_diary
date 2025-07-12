from django.db import models
from rogatkalive import settings


# Create your models here.
class Task(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    done=models.BooleanField(default=False)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    checked_at=models.DateTimeField(blank=True, null=True)