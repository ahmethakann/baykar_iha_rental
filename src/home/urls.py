from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customer_signup/", views.customer_signup, name="customer_signup"),
    path("customer_login/", views.customer_login, name="customer_login"),
    path("iha_dealer_signup/", views.iha_dealer_signup, name="iha_dealer_signup"),
    path("iha_dealer_login/", views.iha_dealer_login, name="iha_dealer_login"),
    path("add_iha/", views.add_iha, name="add_iha"),
    path("edit_iha/<int:myid>/", views.edit_iha, name="edit_iha"),
    path("all_ihas/", views.all_ihas, name="all_ihas"),
    path("delete_iha/<int:myid>/", views.delete_iha, name="delete_iha"),
    path("customer_homepage/", views.customer_homepage, name="customer_homepage"),
    path("search_results/", views.search_results, name="search_results"),
    path("iha_rent/", views.iha_rent, name="iha_rent"),
    path("order_details/", views.order_details, name="order_details"),
    path("past_orders/", views.past_orders, name="past_orders"),
    path("delete_order/<int:myid>/", views.delete_order, name="delete_order"),
    path("all_orders/", views.all_orders, name="all_orders"),
    path("complete_order/", views.complete_order, name="complete_order"),
    path("earnings/", views.earnings, name="earnings"),
    path("signout/", views.signout, name="signout")
]