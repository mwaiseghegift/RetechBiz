from allauth.account.forms import SignupForm
from django import forms
from .models import Profile, Manager

from django.contrib.auth import get_user_model
User = get_user_model()


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    profile_picture = forms.ImageField(label='Display Picture', required=False)

    class Meta:
        model = Profile

    def signup(self,request,user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # for the added display_pic
        user.userprofile.profile_picture = self.cleaned_data.get('profile_pictre')
        user.userprofile.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields =('profile_picture','bio','facebook','twitter','email','linkedin')

class ManagerForm(forms.ModelForm):

    class Meta():
        model = Manager
        fields = ('facebook','twitter','linkedin')
