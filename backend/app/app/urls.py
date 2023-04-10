from django.contrib import admin
from django.urls import path

from app.views.authors_views import add_author, edit_author, list_all_authors
from app.views.customers_views import (
    add_a_customer,
    list_all_customers,
    reactivate_customer,
    search_customer,
    soft_delete_customer,
    update_customer_info,
)
from app.views.exemplaries_views import add_exemplary, list_all_exemplaries, reactivate_exemplary, remove_exemplary
from app.views.loans_views import can_customer_loans, list_all_loans, new_loan, return_loan
from app.views.work_views import add_work, list_all_works, update_work

urlpatterns = [
    path("admin/", admin.site.urls),
    path("customers/", list_all_customers),
    path("customer/<int:customer_id>/", search_customer),
    path("customer/<int:customer_id>/delete", soft_delete_customer),
    path("customer/<int:customer_id>/reactivate", reactivate_customer),
    path("customer/<int:customer_id>/update", update_customer_info),
    path("customer/add", add_a_customer),
    path("authors/", list_all_authors),
    path("author/add", add_author),
    path("author/<int:author_id>/update", edit_author),
    path("works/", list_all_works),
    path("work/add", add_work),
    path("work/<int:work_id>/update", update_work),
    path("exemplaries/", list_all_exemplaries),
    path("exemplary/add", add_exemplary),
    path("exemplary/<int:exemplary_id>/delete", remove_exemplary),
    path("exemplary/<int:exemplary_id>/reactivate", reactivate_exemplary),
    path("loans", list_all_loans),
    path("loans/user/enabled", can_customer_loans),
    path("loans/return", return_loan),
    path("loans/new", new_loan),
]
