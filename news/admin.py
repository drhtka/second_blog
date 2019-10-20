# -*- coding: utf-8 -*-
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from news.models import News, Category, Tag, Coments

class NesAdmin(SummernoteModelAdmin):
    summernote_fields = ('text_min', 'text')

admin.site.register(News, NesAdmin)
admin.site.register(Category)
admin.site.register(Tag)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')

admin.site.register(Coments, CommentAdmin)

