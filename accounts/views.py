from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from .forms import UserProfileForm
from .models import Profile, Manager
from django.views.generic import CreateView,UpdateView,CreateView,DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


class UserProfileCreateView(CreateView):
    model = Profile
    form_class = UserProfileForm

    def form_valid(self, form):
        form.instance.slug = self.request.user.username
        return super().form_valid(form)

class UserProfileView(DetailView):
    model = Profile
    template_name = 'users/user_profile.html'

    
    def get_object(self):
        return self.request.user.related_user

class ProfileUpdateView(UpdateView):
    fields = '__all__'
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('user_profile') #Name of the url

    def get_object(self):
        return self.request.user.userprofile()

class ManagerDetailView(DetailView):
    model = Manager