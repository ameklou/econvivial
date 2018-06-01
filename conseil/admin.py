from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish','status','audio_file_player')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
admin.site.register(Post, PostAdmin)
