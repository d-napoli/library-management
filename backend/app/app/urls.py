from django.contrib import admin
from django.urls import path

from app.views.customers_views import (
    list_all_customers,
    reactivate_customer,
    search_customer,
    soft_delete_customer,
    update_customer_info,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("customers/", list_all_customers),
    path("customer/<int:customer_id>/", search_customer),
    path("customer/<int:customer_id>/delete", soft_delete_customer),
    path("customer/<int:customer_id>/reactivate", reactivate_customer),
    path("customer/<int:customer_id>/update", update_customer_info),
]
