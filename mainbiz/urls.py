from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'mainbiz'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('gallery/create/', views.GalleryCreateView.as_view(), name='gallery_create'),
    path('blog/', views.BlogListView, name='blog_list'),
    path('blog/create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/<uuid:id>/edit/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<uuid:id>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/category/<int:pk>/', views.BlogCategory.as_view(), name='blog_category'),
    path('blog/<uuid:blog_id>/', views.BlogDetail, name='blog-detail'),
    path('results/', views.SearchView, name='blog-search'),
    path('blog/<slug:tag_slug>/', views.TagView, name='tags'),
    path('services/', views.Services, name='services'),
    path('hackinglab/', views.TemplateView.as_view(template_name='hacking_lab.html'), name='hacking_lab'),
    path('videodownloaders/', views.TemplateView.as_view(template_name='video_downloaders.html'), name='downloaders'),
    path('entertainment/', views.EntertainmentView, name='entertainment'),
]
