from django.contrib import admin
from django.urls import path, include
from authentication.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(('authentication.urls','authentication'))),
    path('operations/', include(('operations.urls', 'operations'))),
    path('', home, name="home"),
]
