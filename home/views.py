'''Import model'''
from django.shortcuts import render
from django.views import generic
from django.views.generic import UpdateView
from .models import Post
from home.forms import BlogPostForm
from django.urls import reverse_lazy


class PostList(generic.ListView):
    '''This class handles all posts'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "home/index.html"
    paginate_by = 6


def add_blogs(request):
    if request.method == "POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "home/add_blogs.html", {
                'obj': obj, 'alert': alert
                })
    else:
        form = BlogPostForm()
    return render(request, "home/add_blogs.html", {'form': form})


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'home/edit_blog_post.html'
    fields = ['title', 'slug', 'content', 'featured_image']
    success_url = reverse_lazy('post_details')
