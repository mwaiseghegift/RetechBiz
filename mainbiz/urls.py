from django.urls import path
from . import views

app_name = 'mainbiz'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('gallery/create/', views.GalleryCreateView.as_view(), name='gallery_create'),
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/category/<int:pk>/', views.BlogCategory.as_view(), name='blog_category'),
]
