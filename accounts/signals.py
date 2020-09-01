from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.conf import settings


# def post_save_profile_create(sender, instance, created, *args, **kwargs):
#     if created:
#         Profile.objects.get_or_create(user=instance)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_profile(sender, instance, **kwargs):  12
#     instance.profile.save()