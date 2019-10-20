# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Coments
class CommentForm(ModelForm):
    """Форма комментариев к статье

    """
    class Meta:
        model = Coments
        fields = ('text', )



