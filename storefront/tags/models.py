from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label=models.CharField(max_length=255)

class TaggedItem(models.Model):
    # What tag is applied to what object
    tag=models.ForeignKey(to=Tag, on_delete=models.CASCADE)
    # To create Generic Relationships we need three attributes:
        # 1. content_type
        # 2. object_id
        # 3. content_object
    content_type=models.ForeignKey(to=ContentType, on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey()
