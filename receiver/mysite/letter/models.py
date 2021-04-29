from django.db import models
from django.utils import timezone


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1500)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{{sender={self.sender}, title={self.title}, created={self.created}}}"

    @classmethod
    def create(cls, sender, title, content):
        ret = cls(sender=sender, title=title, content=content)
        return ret

    def to_json(self):
        return {"id": self.id, "sender": self.sender, "title": self.title, "content": self.content}
