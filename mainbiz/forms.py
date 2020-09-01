from django import forms
from .models import Gallery, Blog, Comment
from django.forms import ModelForm

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='Your Name')
    email = forms.EmailField(required=True, label= 'Your Email')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, required=True)

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['name','description','image']

class BlogForm(ModelForm):

    class Meta:
        model = Blog
        exclude = ['image_thumbnail','updated_on']

        widgets = {
            'text': forms.Textarea(attrs={'class':'textarea.tinymce'}),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']