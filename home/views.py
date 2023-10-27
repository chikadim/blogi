'''Import model'''
from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import UpdateView
from .models import Post, Profile, Kind
from home.forms import BlogPostForm, ProfileForm
from django.urls import reverse_lazy


class PostList(generic.ListView):
    '''This class handles all posts'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "home/index.html"
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        cat_menu = Kind.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


'''def list_posts_by_kind(request, slug):
    kind = get_object_or_404(Kind, slug=slug)

    posts = Post.objects.filter(kind=kind)

    context = {"kind_name": kind.name, "posts": posts}

    return render(request, "kind.html", context)'''


'''def list_posts_by_kind(request, slug):
    kind = get_object_or_404(Kind, slug=slug)
    posts = Post.objects.filter(kind=kind)

    return render(request, 'home/kind.html', {'kind_name': kind.name, 'posts': posts})'''


def search_feature(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter Post Model by the search query
        posts = Post.objects.filter(title__contains=search_query)
        return render(request, 'home/search.html', {'search_query': search_query, 'posts': posts})
    else:
        return render(request, 'home/search.html', {})


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


def Delete_Blog_Post(request, slug):
    posts = Post.objects.get(slug=slug)
    if request.method == "POST":
        posts.delete()
        return redirect('/')
    return render(request, 'home/delete_blog_post.html', {'posts': posts})


def user_profile(request, myid):
    profile = Profile.objects.filter(user=myid)
    return render(request, "home/user_profile.html", {'profile': profile})


def see_profile(request):
    return render(request, "home/profile.html")


def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == "POST":
        form = ProfileForm(data=request.POST, files=request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            alert = True
            return render(request, "home/edit_profile.html", {'alert': alert})
    else:
        form = ProfileForm(instance=profile)
    return render(request, "home/edit_profile.html", {'form': form})
