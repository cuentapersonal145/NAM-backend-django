from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from .views import *

router = DefaultRouter()

router.register('tipo', TipoViewSet)
router.register('producto', ProductoViewSet)
router.register('producto-tipo', ProductoTipoViewSet)

urlpatterns = [
    path( 'api/', include(router.urls) )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
