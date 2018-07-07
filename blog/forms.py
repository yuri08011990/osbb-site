from django import forms
from PIL import Image
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'image', 'text',)