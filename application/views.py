from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
import redis as rd
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import MakeModeratorSerializer, UserSerializer, TokenSerializer, AddPointsSerializer
from datetime import timedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .permissions import IsAuthenticated

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    else:
        print("TOKEN INVALID")

class CustomAuthToken(ObtainAuthToken):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        # Validate data
        if not serializer.is_valid(raise_exception=False) and {"username", "password"} <= request.data.keys():
            redis = rd.Redis(
                host='localhost',
                port=6379
            )
            username = request.data['username']
            login_attempts = redis.get(username)
            if login_attempts:
                redis.setex(username, time=timedelta(minutes=30),
                            value=int(login_attempts) + 1)
                if int(login_attempts) + 1 >= 4:
                    return Response({
                        'error': 'login failed',
                        'message': 'exceeded login attempts, try after thirty minutes'
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                redis.setex(username, time=timedelta(minutes=30), value=1)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'email': user.email,
            'nickname': user.nickname,
            'profile': user.profile
        })

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def validate_token(request):
    """
    Validate token
    """
    if request.method == 'POST':
        serializer = TokenSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        token = Token.objects.filter(
            key=serializer.validated_data['token']).first()
        if not token:
            return Response({'valid token': False}, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'token': token.key,
            'valid token': True,
            'nickname': token.user.nickname,
            'email': token.user.email,
            'profile': token.user.profile,
            'points': token.user.points
        })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_points(request):
    serializer = AddPointsSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    token = Token.objects.filter(
        key=serializer.validated_data['token']).first()
    if not token:
        return Response({'status_add_points': 'Invalid token', 'error': True}, status=status.HTTP_400_BAD_REQUEST)

    user = token.user
    user.points += serializer.validated_data['points']

    if user.points == 20:
        user.profile = 'basic'
    if user.points == 100:
        user.profile = 'advanced'
    if user.points == 1000:
        user.profile = 'moderator'
    user.save()
    return Response({
        'add_points': True,
        'nickname': user.nickname,
        'points': user.points,
        'profile': user.profile
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def make_moderator(request):
    serializer = MakeModeratorSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = User.objects.get(email=serializer.validated_data['user_email'])
    user.profile = 'moderator'
    user.points = 1000
    user.save()
    return Response({
        'email': user.email,
        'nickname': user.nickname,
        'profile': user.profile,
        'points': user.points
    })
