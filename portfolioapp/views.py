from django.shortcuts import render,redirect
from .models import *
from .forms import ContactForm
import os
from django.http.response import HttpResponse
import mimetypes
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib import messages


# Create your views here.

def index(request):
    #project section
    projects=Project.objects.all()

    #home section
    home_image=home.objects.all()#get(id=1)

    #contact section
    form=ContactForm()
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.send()
            messages.success(request,"Thanks for your message!")
            return redirect('contact-success')

    #blog section
    category=request.GET.get('category')
    if category== None:
        blogs=Blog.objects.all()
        blogs=blogs.order_by('-id')
       
    else:
         blogs=Blog.objects.filter(category__name__icontains=category)
    categories=Category.objects.all()[:8]
            
    return render(request,'portfolioapp/base.html', {'projects':projects,  'form':form, 'blogs':blogs, 'categories':categories, 'home_image':home_image})


def download_file(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/portfolioapp/static/portfolioapp/file/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'index.html')  


def contact_success(request):
    home_image=home.objects.get(id=1)
    context={'home_image':home_image}
    return render(request, 'portfolioapp/contact_success.html', context)

def project_view(request, portfolio_slug):
    project=Project.objects.get(slug=portfolio_slug)
    more_images=Project_upload.objects.filter(category=project.category.id)
    home_image=home.objects.all()#get(id=1)
   
    context={'project':project, 'images':more_images,  'home_image':home_image}
    return render(request, 'portfolioapp/project_view.html' , context)   

def blog_view(request, blog_slug):
    blog=Blog.objects.get(slug=blog_slug)
    blogs=Blog.objects.all()
    home_image=home.objects.get(id=1)
    categories=Category.objects.all()
    context={'blogs':blogs, 'blog':blog, 'categories':categories, 'home_image':home_image,}
    return render(request, 'portfolioapp/blog_view.html',context )  

def blog_by_category(request, category):
    home_image=home.objects.get(id=1)
    
    if category== None:
        blogs=Blog.objects.filter(category__name=category)
    else:
         blogs=Blog.objects.filter(category__name__icontains=category)
    categories=Category.objects.all()[:8]
    return render(request, 'portfolioapp/blog_by_category.html', {'blogs':blogs, 'categories':categories, 'home_image':home_image,})  

def blog_all(request):
    home_image=home.objects.get(id=1)
    category=request.GET.get('category')
    if category== None:
        blogs=Blog.objects.all()
        blogs=blogs.order_by('-id')
       
    else:
         blogs=Blog.objects.filter(category__name__icontains=category)
    categories=Category.objects.all()[:8]
    
    return render(request, 'portfolioapp/blog_all.html',{ 'home_image':home_image,  'blogs':blogs, 'categories':categories })         

  
        
