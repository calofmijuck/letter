from django.db import models
from django.utils import timezone
# Create your models here.

class Message(models.Model):
    sender = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1500)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sender + ":" + self.title

    @classmethod
    def create(cls, sender, title, content):
        ret = cls(sender=sender, title=title, content=content)
        return ret
