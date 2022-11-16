from unicodedata import category
from django.contrib import admin
from .models import Blog,  Project, Category, Project_upload, home

# Register your models here.

class ProjectAdmin (admin.ModelAdmin):
   list_display=('name', 'category',  )
   list_filter=('category',)
   prepopulated_fields={'slug':('name',)}

class BlogAdmin (admin.ModelAdmin):
   list_display=('title', 'category', 'description', )
   list_filter=('category',)
   prepopulated_fields={'slug':('title',)}
admin.site.register(home)    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Project_upload)
