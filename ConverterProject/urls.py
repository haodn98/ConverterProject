from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import home

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('auth/', include(('authentication.urls', 'authentication'))),
                  path('operations/', include(('operations.urls', 'operations'))),
                  path('subs/', include(('subscriptions.urls', 'subscriptions'))),
                  path('', home, name="home"),
                  path("__debug__/", include("debug_toolbar.urls")),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
