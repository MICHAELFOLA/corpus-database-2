
from django import forms
from .models import Post


class WebForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ('Article_Url', 'Article_Title', 'Words_Per_Column',)