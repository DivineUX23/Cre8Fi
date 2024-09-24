from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ContentViewSet, TransactionViewSet, MessageViewSet, NotificationViewSet, SubscriptionViewSet, SupportTicketViewSet, AnalyticsViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'content', ContentViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'support-tickets', SupportTicketViewSet)
router.register(r'analytics', AnalyticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]