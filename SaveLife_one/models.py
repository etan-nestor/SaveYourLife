from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    text_intro = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='media')
    date_added = models.DateTimeField(default=timezone.now)
    shares = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField()
    name = models.CharField(max_length=100, default='Anonyme')
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_added']
