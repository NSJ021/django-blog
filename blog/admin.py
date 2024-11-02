from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment
# Classes
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Display options for admin panel related to blog posts

    **Context**

    ``list display``
        allows title, slug status and created on for list display properties
    ``search fields``
        allowed search fields, title and content
     ``list filter``
        allowed list filters, status, created on and author
    ``prepopulated``
        prepopulated fields, sluig and title
    ``summernote``
        allows summernote text editor on content field
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'author')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.

#admin.site.register(Post)
admin.site.register(Comment)