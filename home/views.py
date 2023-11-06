'''Import model'''
from django.shortcuts import render, redirect
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import UpdateView, ListView
from .models import Post, Profile, Variety
from home.forms import BlogPostForm, ProfileForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class PostList(generic.ListView):
    '''This class handles all posts'''
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "home/index.html"
    paginate_by = 9

    def get_context_data(self, *args, **kwargs):
        cat_menu = Variety.objects.all().exclude(name='Default')
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu

        return context


# Category list view
class VarietyListView(ListView):
    """
    Variety List view shows the list of categories
    """
    template_name = 'home/variety.html'
    context_object_name = 'varlist'

    def get_queryset(self):
        content = {
            'var': self.kwargs['varieties'],
            'posts': Post.objects.filter(
                varieties__name=self.kwargs['varieties']).filter(status=1)
        }
        return content


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
            messages.success(request, 'Post created successfully')
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return redirect('/', {
                'obj': obj, 'alert': alert
            })
    else:
        form = BlogPostForm()
    return render(request, "home/add_blogs.html", {'form': form})


class UpdatePostView(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'home/edit_blog_post.html'
    fields = ['title', 'slug', 'content', 'varieties', 'featured_image']
    success_message = 'The cocktail was edited successfully!'
    success_url = reverse_lazy('post_details')


def Delete_Blog_Post(request, slug):
    posts = Post.objects.get(slug=slug)
    if request.method == "POST":
        posts.delete()
        return redirect('/')
    return render(request, 'home/delete_blog_post.html', {'posts': posts})


def user_profile(request, myid):
    profile = Profile.objects.filter(user=myid)
    post = Post.objects.all()
    return render(request, "home/user_profile.html",
                  {'profile': profile, 'post': post})


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
            messages.success(request, "You have successfully updated your profile")
            form.save()
            alert = True
            return render(request, "home/edit_profile.html", {'alert': alert})
    else:
        form = ProfileForm(instance=profile)
    return render(request, "home/edit_profile.html", {'form': form})


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    try:
        if created:
            Profile.objects.create(user=instance).save()
    except Exception as err:
        print(f'Error creating user profile!\n{err}')
