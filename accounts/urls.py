from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.UserProfileView.as_view(), name='user_profile'),
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile_update'),
]
