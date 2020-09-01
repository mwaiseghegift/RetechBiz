from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (View, ListView, DetailView, TemplateView,
                                CreateView, UpdateView, DeleteView)
from .models import (Gallery, Service, About, AboutUsService, Category, 
                    Testimonial, Intro, Blog, Comment)
from accounts.models import Manager
from django.utils import timezone
from .forms import ContactForm, CommentForm
from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse,reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def is_users(post_user, logged_user):
    return post_user == logged_user


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'galleries'
    model = Gallery
    paginate_by = 8

    def get_context_data(self, **kwargs):
        data = super(IndexView, self).get_context_data(**kwargs)
        data['intros'] = Intro.objects.all()
        data['services'] = Service.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
        data['abouts'] = About.objects.all()
        data['about_services'] = AboutUsService.objects.all()
        data['form'] = ContactForm
        data['testimonials'] = Testimonial.objects.all()
        data['managers'] = Manager.objects.all()
        return data

    



class GalleryView(ListView):
    model = Gallery
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'galleries'

    def get_queryset(self):
        return Gallery.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    
        
class GalleryCreateView(LoginRequiredMixin, CreateView):
    model = Gallery
    template_name = 'gallery/gallery_form.html'
    fields = ['name','description','image']
    success_url = '/gallery/'

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 10

    def get_queryset(self):
        return Blog.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    

    def get_context_data(self, **kwargs):
        data = super(BlogListView, self).get_context_data(**kwargs)
        data["gallery_feed"] = Gallery.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:6]
        data["categories"] = Category.objects.all()
        data["recent_post"] = Blog.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        return data

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        data = super(BlogDetailView, self).get_context_data(**kwargs)
        data["gallery_feed"] = Gallery.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:6]
        data["categories"] = Category.objects.all()
        data["recent_post"] = Blog.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        data["comments"] = Comment.objects.filter(post=self.get_object()).order_by('created_date')
        data["form"] = CommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment=Comment(content=request.POST.get('content'),
                            author=self.request.user,
                            post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('mainbiz:blog_detail')

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title','image','category','content','text','source','source_link','slug','pub_date']
    redirect_field_name = 'blog/blog_list.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Oops, Make sure everything is ok')
        return super().form_invalid(form)

class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['title','image','category','content','text','source','source_link']
    redirect_field_name = 'blog/blog_detail.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.updated_on = timezone.now()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Oops, Make sure everything is ok")
        return super().form_invalid(form)

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('mainbiz:blog_list')

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)

class BlogCategory(ListView):
    model = Blog
    template_name = 'blog/blog_category.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Blog.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        data = super(BlogCategory, self).get_context_data(**kwargs)
        data["gallery_feed"] = Gallery.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:6]
        data["categories"] = Category.objects.all()
        data["recent_post"] = Blog.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        data['category'] = self.category
        return data
    
    
 
    


