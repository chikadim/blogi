from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))


class Profile(models.Model):
    """
    This class builds the Profile Model
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    profile_image = CloudinaryField('image', default='placeholder')
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)


class Variety(models.Model):
    """
    Model for Variety
    """
    class Meta:
        verbose_name_plural = "varieties"
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

    """Sets absolute URL"""
    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    '''This model handles all posts'''

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    varieties = models.ForeignKey(
        Variety, on_delete=models.SET_DEFAULT, default=5)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    objects = None

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    '''This model handles comments'''

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
