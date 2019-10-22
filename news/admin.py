# -*- coding: utf-8 -*-
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from news.models import News, Category, Tag, Coments

class NesAdmin(SummernoteModelAdmin):
    list_display = ('title', 'user', 'created',)
    list_filter = ('user', 'created',)
    list_editable = ('user', )
    search_fields = ['title', 'user__username',]
    summernote_fields = ('text_min', 'text',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')

admin.site.register(News, NesAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Coments, CommentAdmin)

