'''Import model'''
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    '''This class handles all posts'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "home/index.html"
    paginate_by = 6
