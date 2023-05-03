from django.urls import path

from .views import(
    product_detail_view, 
    product_create_view,
    dymanic_lookup_view,
    product_delete_view,
    product_list_view
)
app_name = 'products '
urlpatterns = [
   
    path("product/", product_detail_view),
    path("create/", product_create_view),
    path("lookup/<int:my_id>", dymanic_lookup_view,name='product_lookup'),
    path("delete/<int:my_id>", product_delete_view),
    path("list/", product_list_view,name='product_list'),
]