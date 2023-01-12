from django.urls import path
from . import views # import 길이가 길어지는 걸 막기 위함

urlpatterns = [
    path("", views.movie_list),
    path("review/<int:pk>", views.post_read),
    path("review/create", views.post_create),
    path("review/<int:pk>/delete", views.post_delete),
    path("review/<int:pk>/edit", views.post_edit),
]
