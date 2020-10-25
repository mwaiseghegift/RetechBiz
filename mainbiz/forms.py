from django import forms
from .models import Gallery, Blog, Comment
from django.forms import ModelForm

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs=({'class':'col-12 form-group form-control valid','id':'name', 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Enter your name'"})
            ) ,max_length=50, label='Your Name')
    your_email = forms.EmailField(widget=forms.TextInput(
        attrs=({'class':'col-12 form-group form-control valid','id':'email','type':'email', 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Enter email address'"})
            ), required=True, label= 'Your Email')
    subject = forms.CharField(widget=forms.TextInput(
        attrs=({'class':'col-12 form-group form-control', 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Enter the subject'"})
            ), max_length=100)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class':'col-12 form-group form-control w-100','id':'message', 'cols':"30", 'rows':"9", 'onfocus':"this.placeholder = ''", 'onblur':"this.placeholder = 'Input your message'"}
            ), required=True)
 

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