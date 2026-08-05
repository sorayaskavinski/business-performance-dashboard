from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search_sales, name="search_sales"),
    path("update/<str:sale_id>/", views.update_sale_view, name="update_sale"),
    path("delete/<str:sale_id>/", views.delete_sale_view, name="delete_sale"),
    path("add/", views.add_sale_view, name="add_sale"),
]