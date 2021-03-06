"""authors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Author's Haven For Team Invictus",
      default_version='v1',
      description="Author's Haven is a community of like minded authors to \
        foster inspiration and innovation by leveraging the modern web",
      license=openapi.License(name="Andela License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=(),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authors.apps.authentication.urls')),
    path('api/', include('authors.apps.articles.urls')),
    path('api/', include('authors.apps.profiles.urls')),
    path('api/', include('authors.apps.comments.urls')),
    path('api/articles/', include('authors.apps.favorites.urls')),
    path('api/', include('authors.apps.rate_article.urls')),
    path('api/', include('authors.apps.article_tags.urls')),
    path('api/', include('authors.apps.bookmarks.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('authors.apps.notifications.urls'))
]
