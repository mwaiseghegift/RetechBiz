from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from . import forms
from django.contrib import messages
from .forms import ProfileUpdateForm, UserUpdateForm
from .models import Profile, Manager
from django.views.generic import CreateView,UpdateView,CreateView,DetailView,ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.   

class ManagerDetailView(ListView):
    model = Manager
    template_name = 'users/user_profile.html'

    def get_object(self):
        return Manager.objects.filter(user=User)

# class UserProfileView(DetailView):
#     model = Profile
#     template_name = 'users/user_profile.html'

    
#     def get_object(self):
#         return self.request.user.profile

class UserProfileUpdateView(UpdateView):
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('profiles:user_profile')

    def get_object(self):
        return self.request.user.profile

    

class ProfileView(DetailView):
    template_name = 'users/user_profile.html'
    queryset = User.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('username')
        user = get_object_or_404(User, username=id_)
        return user.profile

@login_required
def ProfileEdit(request, username):

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'profile updated successfully')
            return redirect('profiles:profile_details', request.user.username)

    else:
        p_form = ProfileUpdateForm(instance = request.user.profile)
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'p_form':p_form,
        'u_form':u_form,
    }

    return render(request, 'users/profile_update.html', context)