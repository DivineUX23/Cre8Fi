from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User, Content, Transaction, Message, Notification, Subscription, SupportTicket, Analytics

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_creator', 'is_project_manager', 'is_verified')
    list_filter = ('is_creator', 'is_project_manager', 'is_verified')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('is_creator', 'is_project_manager', 'is_verified', 'bio', 'profile_picture')}),
    )

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'price', 'category', 'created_at', 'views')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description', 'creator__username')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'content', 'amount', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('buyer__username', 'content__title')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'content')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')
    search_fields = ('user__username', 'message')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'start_date', 'end_date', 'is_active')
    list_filter = ('plan', 'is_active', 'start_date', 'end_date')
    search_fields = ('user__username', 'plan')

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'created_at', 'resolved')
    list_filter = ('resolved', 'created_at')
    search_fields = ('user__username', 'subject', 'description')

@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('content', 'views', 'sales', 'revenue', 'date')
    list_filter = ('date',)
    search_fields = ('content__title',)