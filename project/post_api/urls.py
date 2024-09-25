from django.urls import path
from .views import PostCreateView, CommentCreateView, ReplyCreateView

urlpatterns = [
    path("posts/", PostCreateView.as_view(), name="create-post"),
    path(
        "posts/<int:post_id>/comments/",
        CommentCreateView.as_view(),
        name="create-comment",
    ),
    path(
        "comments/<int:comment_id>/replies/",
        ReplyCreateView.as_view(),
        name="create-reply",
    ),
]
