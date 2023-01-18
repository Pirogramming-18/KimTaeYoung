from django.urls import path
from . import views


app_name = "apps"

urlpatterns = [
    path('', views.main_page, name = "idea_list"),
    path('idea/detail/<int:pk>', views.idea_detail, name = "idea_detail"),
    path('idea/create', views.create_idea, name = "create_idea"),
    path('idea/update/<int:pk>', views.update_idea, name = "update_idea"),
    path('idea/delete/<int:pk>', views.delete_idea, name = "delete_idea"),
    path('tool', views.dev_list, name = "dev_list"),
    path('tool/create/', views.dev_create, name = "dev_create"),
    path('tool/detail/<int:pk>', views.dev_detail, name = "dev_detail"),
    path('tool/update/<int:pk>', views.dev_update, name = "dev_update"),
    path('tool/delete/<int:pk>', views.dev_delete, name = "dev_delete"),





]

