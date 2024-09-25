from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser, Group , Permission


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=50)
    firstname = models.CharField(null=True, blank=True, max_length=50)
    lastname = models.CharField(null=True, blank=True, max_length=50)
    is_creator = models.BooleanField(default=False)
    is_project_manager = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_premuim = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    followers = models.ManyToManyField(
        "self", related_name="following", symmetrical=False, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Specify related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_auth",  # Change this to a unique name
        blank=True,
        help_text="The groups this user belongs to",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_perm",  # Change this to a unique name
        blank=True,
        help_text="Specific permissions user.",
        verbose_name="user permissions",
    )

    def follow(self, user):
        if user not in self.following.all():
            self.following.add(user)

    def unfollow(self, user):
        if user in self.following.all():
            self.following.remove(user)

    def is_following(self, user):
        return user in self.following.all()

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField(blank=True)
    avater = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True)
    back_pic = models.ImageField(upload_to="back_pic/", blank=True, null=True)
    ratings = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
