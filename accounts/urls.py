from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    # path('', views.UserProfileView.as_view(), name='user_profile'),
    path('<str:username>/', views.ProfileView.as_view(), name='profile_details'),
    path('<str:username>/update/', views.ProfileEdit, name='edit-profile'),
]
