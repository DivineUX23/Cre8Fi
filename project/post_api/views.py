from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in user
        serializer.save(author=self.request.user)


# Create Comment API
class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Attach the comment to the post (using the post_id passed in the URL)
        post = Post.objects.get(id=self.kwargs["post_id"])
        serializer.save(author=self.request.user, post=post)


# Create Reply API
class ReplyCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Attach the reply to the comment (using the comment_id passed in the URL)
        comment = Comment.objects.get(id=self.kwargs["comment_id"])
        serializer.save(author=self.request.user, post=comment.post, parent=comment)
