from django.urls import path
from . import views

app_name = 'mainbiz'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('gallery/create/', views.GalleryCreateView.as_view(), name='gallery_create'),
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    # path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/<uuid:id>/edit/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<uuid:id>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/category/<int:pk>/', views.BlogCategory.as_view(), name='blog_category'),
    path('blog/<uuid:blog_id>/', views.BlogDetail, name='blog-detail'),
    path('results/', views.BlogSearch, name='blog-search'),
]
