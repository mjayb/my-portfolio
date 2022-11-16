from django.db import models
#from phone_field import PhoneField
#from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class home(models.Model):
    image=models.ImageField(upload_to='home_images')
 

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


#Project section
class Project(models.Model):
    name = models.CharField(max_length=50, default='name')
    description = models.TextField(max_length=1000, default='description')
    slug=models.SlugField(unique=True, default='slug')
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False, default=1)
    image = models.ImageField(upload_to='project_images') 
    project_link = models.URLField(max_length=250, null=True, blank=True, default='url' )
    githublink = models.URLField(max_length=250, null=True, blank=True, default='url')

    def __str__(self):
        return self.name


class Project_upload(models.Model):
    title=models.CharField(max_length=100, null=False, blank=False)
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False, default=1)
    image=models.ImageField(upload_to='project_upload_images')

    def __str__(self):
        return self.title


class Blog(models.Model):
    title=models.CharField(max_length=100, null=False, blank=False)
    description=models.TextField()
    slug=models.SlugField(unique=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False, default=1)
    image=models.ImageField(upload_to='blog_images')
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    


 #Contact section
#class Contact(models.Model, ):
    #name = models.CharField(max_length=50)
    #email = models.EmailField(max_length=254, unique=True, null=True)
    #phone_number = PhoneNumberField(blank=True, help_text='Contact phone number')
    #phone = PhoneField(blank=True, help_text='Contact phone number')
    #link = models.URLField(max_length=250)

    #def __str__(self):
          #return f'{self.name}-({self.email})'       
            

                  
