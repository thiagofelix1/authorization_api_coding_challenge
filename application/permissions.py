from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import APIException
from rest_framework import status

class IsAuthenticated(permissions.BasePermission):
    """
    Custom Permission to check if the request comes from movie_api
    """
    def has_permission(self, request, view):
        if not 'HTTP_TOKEN' in request.META:
            return False
        key = 'e907826fa8b7e7899f48516b2a6758be'
        token = request.META['HTTP_TOKEN']
        if token == key:
            return True
        else:
            raise TokenNotExists()

class TokenNotExists(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {'error': True, 'message': 'invalid token'}
    default_code = 'not_access'