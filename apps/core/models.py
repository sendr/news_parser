from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    url = models.URLField()
    site = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'
