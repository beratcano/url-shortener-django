from django.db import models

# Create your models here.
class URL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"