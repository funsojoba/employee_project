import uuid
from django.db import models


def generate_id():
    return uuid.uuid4().hex


class BaseAbstractModel(models.Model):
    id = models.CharField(
        primary_key=True, editable=False, default=generate_id, max_length=70
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_at",)

    def save(self, actor=None, *args, **kwargs):
        if not self.pk:
            self.created_by = actor
        super(BaseAbstractModel, self).save(*args, **kwargs)
