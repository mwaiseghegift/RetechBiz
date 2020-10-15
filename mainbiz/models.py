from django.db import models
from PIL import Image
from django.conf import settings
from accounts.models import Manager
from django_mysql.models import ListCharField
from django.urls import reverse
from django.utils import timezone
#for the ImageKit
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from django.contrib.auth import get_user_model
User = get_user_model()

from tinymce.models import HTMLField

from django.utils.text import slugify
import uuid #ndo tuwe na id ndefu

# Create your models here.
class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gallery_user', null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256)
    image = models.ImageField(upload_to='images/Portfolio/%Y/%m/%d')
    image_thumbnail = ImageSpecField(source='image',
                            processors=[ResizeToFill(800,600)],
                            format='JPEG',
                            options={'quality':50})
    feed_thumbnail = ImageSpecField(source='image',
                            processors=[ResizeToFill(100,100)],
                            format='JPEG',
                            options={'quality':50})
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("gallery")
    
    

class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256)
    image = models.CharField(max_length=100, default='fa fa-bar-chart')
    available = models.BooleanField(default=True)
    link = models.CharField(default='#', max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.name
    

class Testimonial(models.Model):
    text = models.TextField(max_length=256)
    image = models.ImageField(upload_to='images/Testimonials/%Y/%m/%d')
    user = models.ForeignKey(User, related_name='testimonial_user', on_delete=models.CASCADE)
    category = models.CharField(max_length=50, default='Member')
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.text+' - '+self.user.username
    
class Achievement(models.Model):
    image = models.ImageField(upload_to='images/Achievement/%Y/%m/%d')
    description = models.CharField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class CEO(models.Model):
    pass
    
class About(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/AboutUs')

    def __str__(self):
        return self.title

class AboutUsService(models.Model):
    connected_post = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_service')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/clients')

    def __str__(self):
        return self.name


#intro_courasel
class Intro(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=50, null=True, blank=True)
    image1 = models.ImageField(upload_to='images/intro')
    image2 = models.ImageField(upload_to='images/intro')
    image3 = models.ImageField(upload_to='images/intro')
    image4 = models.ImageField(upload_to='images/intro')
    image5 = models.ImageField(upload_to='images/intro')
    image1_thumbnail = ImageSpecField(source='image1',
                        processors=[ResizeToFill(1920,900)],
                        format='JPEG', options={'quality':50})
    image2_thumbnail = ImageSpecField(source='image2',
                        processors=[ResizeToFill(1920,900)],
                        format='JPEG', options={'quality':50})
    image3_thumbnail = ImageSpecField(source='image3',
                        processors=[ResizeToFill(1920,900)],
                        format='JPEG', options={'quality':50})
    image4_thumbnail = ImageSpecField(source='image4',
                        processors=[ResizeToFill(1920,900)],
                        format='JPEG', options={'quality':50})
    image5_thumbnail = ImageSpecField(source='image5',
                        processors=[ResizeToFill(1920,900)],
                        format='JPEG', options={'quality':50})    
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    link = models.CharField(max_length=150, blank=True)
    
    def __str__(self):
        return self.name

    @property
    def no_of_blogs(self):
        return Blog.objects.filter(category=self).count()

class Tag(models.Model):
    title = models.CharField(max_length=200, verbose_name='Tag')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_plural='Tags'

    def get_absolute_url(self):
        return reverse("mainbiz:tags", arg=[self.slug])
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)    
       
    

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title  = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, max_length=50, related_name='category',
                                on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/blog/%Y/%m/%d')
    image_thumbnail = ImageSpecField(source='image', 
                            processors=[ResizeToFill(720,375)],
                            format='JPEG',
                            options={'quality':80})
    feed_thumbnail = ImageSpecField(source='image',
                        processors=[ResizeToFill(70,70)],
                        format='JPEG',
                        options={'quality':60})
    content = models.TextField()
    text = HTMLField(null=True, default='')
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    source = models.CharField(max_length=50)
    source_link = models.URLField(default='#')
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title+' by '+self.author.username

    class Meta:
        ordering = ['-pub_date']

    @property
    def no_of_comments(self):
        return Comment.objects.filter(post=self).count()

    def get_absolute_url(self):
        return reverse("mainbiz:blog-detail", args=[str(self.id)]) 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    parent=models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    # def get_absolute_url(self):
    #     return reverse("blog-detail", kwargs={'blog_id':self.blog.id})
    

    def __str__(self):
        return self.author.username +' - '+self.content

    def replies(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent != None:
            return False
        return True
    
    

