from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)  # ①
    author = models.ForeignKey(User, related_name="blog_posts", on_delete=models.CASCADE)  # ②
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:  # ③
        ordering = ("-publish",)

    def __str__(self):
        return self.title