from django.urls import path
from products.views import (
        product_detail_view,
        product_create_view,
        dynamic_lookup_view,
        product_delete_view,
        product_list_view
        )

app_name = 'products'
urlpatterns = [
        path('<int:id>/', product_detail_view, name='product'),
        path('create/', product_create_view, name='create'),
        path('<int:id>/update/', dynamic_lookup_view, name='product-detail'),
        path('<int:id>/delete/', product_delete_view, name='product'),
        path('', product_list_view, name='product-list'),
]