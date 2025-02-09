from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clientes import views

router = DefaultRouter()
router.register(r'tipos-documento', views.DocumentTypeViewSet)
router.register(r'clientes', views.ClientViewSet)
router.register(r'compras', views.PurchaseViewSet)


urlpatterns = [
    path('buscar-cliente/', views.get_client, name='buscar_cliente'),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path('api/exportar-cliente/<int:cliente_id>/', views.export_client, name='exportar_cliente'),
    path('api/reporte-fidelizacion/', views.loyalty_report, name='reporte_fidelizacion'),

]
