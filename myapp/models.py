from django.db import models
from ckeditor.fields import RichTextField
import uuid

# Create your models here.

class BannerModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    image = models.ImageField(upload_to='banner/')
    tagline = RichTextField()
    title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)