from django.contrib import admin
from .models import Post, Comment, Profile, Variety
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'featured_image',
        'varieties',
        'slug',
        'status',
        'created_on'
        )
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'varieties')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = (
        'user',
        'profile_image',
        'bio', 'phone_no',
        'facebook',
        'instagram',
        'linkedin'
    )


@admin.register(Variety)
class Variety(admin.ModelAdmin):
    list_display = ('cat_id', 'name')
    search_fields = ('cat_id', 'name')
