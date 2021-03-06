"""webshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from tienda_venta import views
from tienda_venta.models import Cliente2
from tienda_venta import views

'''from django.conf.urls import url, include'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include('tienda_almacen.urls')),
    path('api/v1.0/', include('tienda_venta.urls')),
    path('busca/<contra>/<cedula>/', views.ClienteLogin.as_view()),
    path('buscaCate/<categoria>/', views.GetTodo.as_view()),
    path('buscaProdu/<clave>/', views.GetProducto.as_view()),
    path('traeRopa/', views.GetRopa.as_view()),
    path('traeJuegos/', views.GetVideoJuegos.as_view()),
    path('traeCelulares/', views.GetPhone.as_view()),
    path('traeTeles/', views.GetTeles.as_view()),
    path('stock/<int:id_producto>/', views.GetStock.as_view()),
    path('edita/<int:pk>/<int:cantidad_producto>/', views.UpdateProductos.as_view()),
    path('restaura/<int:pk>/<int:cantidad_producto>/',views.RestauraProductos.as_view()),
    path('editaTABLA/<int:productos_id>/<int:pedidos>/', views.AlteraPseudoJoi.as_view()),
    path('buscaP/<cedula>/',views.MandaProductosComprados.as_view()),
    path('buscaPofertados/<cedula>/',views.MandaProductosenVenta.as_view()),
    path('buscaPvendidos/<cedula>/',views.MandaProductosenVendidos.as_view()),
    path('descuento/<id_producto>/<precio_unidad>/', views.Descuentos.as_view()),




  

]


'''
 path('busca', views.ClienteLogin.as_view())
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1.0/',include('tienda_venta.urls'))
]'''


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    