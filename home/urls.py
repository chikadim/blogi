from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
]
