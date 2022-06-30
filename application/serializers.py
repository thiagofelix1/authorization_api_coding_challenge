from application.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = serializers.CharField(read_only=True)
    points = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('email', 'nickname', 'first_name', 'last_name', 'password', 'profile', 'points')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class AddPointsSerializer(serializers.Serializer):
    points = serializers.IntegerField()
    key = serializers.CharField()
    token = serializers.CharField()


class MakeModeratorSerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    token_moderator = serializers.CharField()

    def validate_token_moderator(self, value):
        token_obj = Token.objects.filter(key=value).first()
        if not token_obj or token_obj.user.profile != 'moderator':
            raise serializers.ValidationError(
                "Token does not belong to a moderator ")
        else:
            return value

    def validate_user_email(self, value):
        user_obj = User.objects.filter(email=value).first()
        if not user_obj:
            raise serializers.ValidationError(
                "User not exists")
        if user_obj.profile == 'moderator':
            raise serializers.ValidationError(
                "User is already a moderator")
        return value
