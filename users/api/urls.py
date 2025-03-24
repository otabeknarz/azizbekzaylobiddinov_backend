from django.urls import path
from . import views

urlpatterns = [
    path("get/users-id/", views.get_users_id),
    path("get/", views.get_users),
    path("get/<str:id>/", views.get_user),
    path("add/", views.add_user),
    path("update/", views.update_or_add_user),
]
