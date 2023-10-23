from .models import Comment
from django import forms
from home.models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'featured_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Content of the Blog'}),
        }
