
from django.contrib import admin
from django.urls import path
from miApp import views
from django.conf import settings
from django.conf.urls.static import static

    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', views.tu_vista_principal, name='tu_vista_principal'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('', views.tu_vista_principal, name='home'), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
