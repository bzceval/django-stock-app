from django.contrib import admin
from django.urls import path,  include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('stock/', include('stock.urls')),
]

# STATIC/MEDIA:
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# --------------------------------------------------------
# Swagger + Redoc + Debug
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
   openapi.Info(
      title = "Stock API",
      description = "Stock API Description",
      default_version = 'v1.0',
      contact = openapi.Contact(email="clarusway@clarusway.com"),
      license = openapi.License(name="BSD License"),
   ),
   public = True,
   permission_classes = [AllowAny],
)

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('__debug__/', include('debug_toolbar.urls')), # django-debug-toolbar
]