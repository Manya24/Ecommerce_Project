from django.urls import path,include
from core import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("add_product", views.add_product, name="add_product"),
    path("product_desc/<pk>", views.product_desc, name="product_desc"),
    path("add_to_cart/<pk>", views.add_to_cart, name="add_to_cart"),
    path("orderlist", views.orderlist, name="orderlist"),
    path("checkout_page", views.checkout_page, name="checkout_page"),
    path("add_item/<int:pk>", views.add_item, name="add_item"),
    path("remove_item/<int:pk>", views.remove_item, name="remove_item"),
    path("payment", views.payment, name="payment"),
    path("handlerequest", views.handlerequest, name="handlerequest"),
    path("invoice", views.invoice, name="invoice"),
     path('silk/', include('silk.urls', namespace='silk')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)