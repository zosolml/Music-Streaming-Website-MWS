from django.contrib import admin
from .models import song_thumb,Comment

# Register your models here.
admin.site.register(song_thumb)


class PostAdmin(admin.ModelAdmin):
    list_display = ('song_title', 'slug', 'artist',)
    list_filter =('song_title', 'slug', 'artist',)
    search_fields = ('song_title', 'artist')
    prepopulated_fields = {'slug': ('song_title',)}
    raw_id_fields = ('uploaded_by',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
