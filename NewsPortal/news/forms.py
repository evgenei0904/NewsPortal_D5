from django import forms
from .models import Post, User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'postCategory',
        ]


class AuthorForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  ]

