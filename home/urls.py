from . import views
from django.urls import path
from .views import UpdatePostView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
]
