from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TubeItem(models.Model):
    id = models.AutoField(primary_key=True)
    # title = models.AutoField(max_length=255)
    url = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.url
