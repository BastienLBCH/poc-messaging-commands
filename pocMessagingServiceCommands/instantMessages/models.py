from django.db import models
import uuid


# Create your models here.
class userCreatedConversation(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=100)
    name = models.CharField(max_length=100)
    creator_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


