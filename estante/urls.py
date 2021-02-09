from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from .views import *

router = DefaultRouter()

router.register('tipo', TipoViewSet)
router.register('categoria', CategoriaViewSet)
router.register('marca', MarcaViewSet)
router.register('producto', ProductoViewSet)

urlpatterns = [
    path( 'api/', include(router.urls) ),
    path( 'api/productos/marca/<int:id>/', DatosProductoAPI.as_view() )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
