from django.db import models


class BaseModel(models.Model):
    created_dttm = models.DateTimeField(auto_now_add=True)
    updated_dttm = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_dttm",)

    def has_changes(self, **kwargs):
        a = any(getattr(self, k) != v for k, v in kwargs.items())
        return a

    def save_changes_if_has(self, **kwargs):
        if self.has_changes(**kwargs):
            for field, value in kwargs.items():
                setattr(self, field, value)
            self.save()
