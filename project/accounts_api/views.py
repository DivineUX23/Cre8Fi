from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreationSerializer
from .models import CustomUser
from .serializers import FollowSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class UserRegistrationView(generics.CreateAPIView):
    # permission_classes = [AllowAny]
    # def post(self, request):
    #     serializer = UserCreationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    queryset = CustomUser.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]


class FollowUserView(APIView):
    def post(self, request):
        serializer = FollowSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(
                {"message": "You are now following the user."},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnfollowUserView(APIView):
    def post(self, request):
        user = request.user
        following_user_id = request.data.get("following_user_id")

        try:
            following_user = CustomUser.objects.get(id=following_user_id)
            user.unfollow(following_user)
            user.save()
            return Response(
                {"message": "You have unfollowed the user."}, status=status.HTTP_200_OK
            )
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )


# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(
#             data=request.data, context={"request": request}
#         )
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data["user"]
#         token, created = Token.objects.get_or_create(user=user)

#         # Update last login time
#         update_last_login(None, user)

#         return Response(
#             {
#                 "token": token.key,
#                 "user_id": user.pk,
#                 "email": user.email,
#                 "username": user.username,
#                 "is_active": user.is_active,
#             },
#             status=status.HTTP_200_OK,
#         )
