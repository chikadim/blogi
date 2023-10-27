from . import views
from django.urls import path
from .views import UpdatePostView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),
    path("search/", views.search_feature, name="search-view"),
    path('vat/<int:id>/', views.PostList.as_view(), name="variety-index"),


    # profile
    path("profile/", views.see_profile, name="profile"),
    path("user_profile/<int:myid>/", views.user_profile, name="user_profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
]
