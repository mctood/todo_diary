from django.db import models
from rogatkalive import settings


# Create your models here.
class Note(models.Model):
    class Moods:
        GOOD = "good"
        BAD = "bad"

        choices = (
            (GOOD, "Good"),
            (BAD, "Bad"),
        )

    id = models.AutoField(primary_key=True)
    content = models.TextField()
    mood = models.CharField(choices=Moods.choices)
    date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)