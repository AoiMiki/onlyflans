from django.db import models
import uuid

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    img_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    customer_email = models.EmailField(max_length = 150)
    customer_name = models.CharField(max_length = 64)
    message = models.TextField()