from app.views.authors_views import add_author, edit_author, list_all_authors
from app.views.customers_views import (
    add_a_customer,
    list_all_customers,
    reactivate_customer,
    search_customer,
    soft_delete_customer,
    update_customer_info,
)
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("customers/", list_all_customers),
    path("customer/<int:customer_id>/", search_customer),
    path("customer/<int:customer_id>/delete", soft_delete_customer),
    path("customer/<int:customer_id>/reactivate", reactivate_customer),
    path("customer/<int:customer_id>/update", update_customer_info),
    path("customer/add", add_a_customer),
    path("authors", list_all_authors),
    path("author/add", add_author),
    path("author/<int:author_id>/update", edit_author),
]
