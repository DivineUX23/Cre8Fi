from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField(
        max_length=500, blank=True, null=True
    )  # Content of the post
    photo = models.ImageField(
        upload_to="post_photos/", blank=True, null=True
    )  # Photo upload
    video = models.FileField(
        upload_to="post_videos/", blank=True, null=True
    )  # Video upload
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="liked_posts", blank=True
    )
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return f"Post by {self.author.username}"

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )  # Post the comment is related to
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )  # Author of the comment
    content = models.TextField(max_length=300)  # Content of the comment
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )  # Parent comment for replies
    is_approved = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post}"



