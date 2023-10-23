from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostDetails.as_view(), name='post_details'),
    path('<slug:slug>/', views.PostDetails.as_view(), name='post_details'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
