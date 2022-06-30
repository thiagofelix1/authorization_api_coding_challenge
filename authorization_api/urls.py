from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from application import views
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('signup', views.UserCreateAPIView.as_view()),
    path('api-token-valid/', views.validate_token),
    path('add-points/', views.add_points),
    path('make-moderator/', views.make_moderator),
    path('openapi', get_schema_view(
        title="Authorization Api",
        description="Authorization api for comment and score system Code challenge Itaú",
        version="1.0.0"
    ), name='openapi-schema'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
