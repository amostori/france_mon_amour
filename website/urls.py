from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<post_id>', views.delete_post, name='delete_post'),
    path('edit/<post_id>', views.edit_post, name='edit_post'),
    path('example', views.example, name='example'),
]
