from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_creator = models.BooleanField(default=False)
    is_project_manager = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

class Content(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_content')
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='content/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)  # Comma-separated tags
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

class Transaction(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class SupportTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_tickets')
    subject = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

class Analytics(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='analytics')
    views = models.PositiveIntegerField(default=0)
    sales = models.PositiveIntegerField(default=0)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateField(auto_now_add=True)