from django.db import models
from django.conf import settings
from . validators import phone_regex

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.title

class Author(models.Model):
    phone = models.CharField(max_length=255, validators=[phone_regex])
    birth_date = models.DateField(null=True)
    topic = models.CharField(max_length=255, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

class Post(models.Model):
    POST_STATUS_PUBLISH = 'P'
    POST_STATUS_DRAFT = 'D'
    POST_STATUS_CHOICES = [
        (POST_STATUS_PUBLISH, 'Publish'),
        (POST_STATUS_DRAFT, 'Draft')
    ]
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')
    slug = models.SlugField(blank=True)
    content = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=POST_STATUS_CHOICES,  default=POST_STATUS_DRAFT)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)



