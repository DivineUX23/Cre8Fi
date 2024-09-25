from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "firstname",
            "lastname",
            "password",
            "is_staff",
            "is_active",
            "is_superuser",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_staff": {"read_only": True},
            "is_active": {"read_only": True},
            "is_superuser": {"read_only": True},
        }

    def create(self, validated_data):
        # Check if we are creating a superuser or a regular user
        if validated_data.get("is_superuser"):
            user = CustomUser(
                username=validated_data["username"],
                email=validated_data["email"],
                firstname=validated_data["firstname"],
                lastname=validated_data["lastname"],
                is_staff=True,
                is_active=True,
                is_superuser=True,
            )
        else:
            user = CustomUser(
                username=validated_data["username"],
                email=validated_data["email"],
                is_staff=False,  # Regular users should not be staff
                is_active=True,
                is_superuser=False,
            )

        # Set the hashed password
        user.set_password(validated_data["password"])
        user.save()
        return user


class FollowSerializer(serializers.Serializer):
    following_user_id = serializers.IntegerField()

    def validate_following_user_id(self, value):
        try:
            return CustomUser.objects.get(id=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")

    def create(self, validated_data):
        user = self.context["request"].user
        following_user = validated_data["following_user_id"]
        user.follow(following_user)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is inactive.")
                data["user"] = user
            else:
                raise serializers.ValidationError("Invalid credentials.")
        else:
            raise serializers.ValidationError('Must include "email" and "password".')
        return data
