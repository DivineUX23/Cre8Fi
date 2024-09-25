user = CustomUser.objects.get(id=user_id)
followers = user.followers.all()  # Get all followers
following = user.following.all()   # Get all users this user is following




post = Post.objects.get(id=post_id)
comments = post.comments.all()

comment = Comment.objects.get(id=comment_id)
replies = comment.replies.all()