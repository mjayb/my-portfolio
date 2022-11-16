from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<str:portfolio_slug>', views.project_view, name='project-view'),
    path('download/<str:filename>', views.download_file, name='download'),
    path('success', views.contact_success, name='contact-success'),
    path('blog-view/<str:blog_slug>', views.blog_view, name='blog-view'),
    path('blog-by-category/<str:category>', views.blog_by_category, name='blog-by-category'),
    path('blogs', views.blog_all, name='blog_all'),
    
]