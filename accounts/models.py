from django.db import models
from django.conf import settings
from django.contrib import auth
from PIL import Image 
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.urls import reverse
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()
   
CATEGORY = (
    ('CEO','Chief Executive Office'),
    ('PM', 'Production Manager'),
    ('CTO', 'CTO'),
    ('Acc','Accountant'),
    ('Member','Member'),
)

class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY, max_length=100)
    image = models.ImageField(upload_to='images/committee', default='images/committee/me.jpg')
    image_thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(500,500)],
                                format='JPEG',
                                options={'quality':50})
    twitter = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    google = models.EmailField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username+''+self.category

    def get_absolute_url(self):
        return reverse("manager_details", kwargs={"pk": self.pk})
    
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/profile_pics/%Y/%m/%d', default='images/profile_pics/default.png')
    image_thumbnail = ImageSpecField(
                            source='profile_picture',
                            processors=[ResizeToFill(300,300)],
                            format='JPEG',
                            options={'quality':80})
    status = models.CharField(max_length=256, null=True, blank=True)
    category = models.CharField(choices=CATEGORY, max_length=50, default='Member')
    bio = models.TextField(max_length=1000, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profiles:user_profile", kwargs={"slug": self.slug})
    
    

    

