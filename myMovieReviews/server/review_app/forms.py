from django import forms
from .models import Post





class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'released_year', 'genre', 'star_rating', 'review', 'director', 'actor', 'time',)

