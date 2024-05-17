from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Testimonial(models.Model):
    name=models.CharField(max_length=250)
    position=models.CharField(max_length=250)
    image=models.ImageField(upload_to="testimonial/")
    description=models.TextField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

    
class Course(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to="course/")
    description=HTMLField()

    def __str__(self):
        return self.title


class CourseFeactures(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return self.title


class CourseOverview(models.Model):
    CHOICE = (("overview", "Overview"), ("training_structure", "Training Structure"),("eligibility", "Eligibility"),("facilities", "Facilities"))
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(choices=CHOICE,max_length=200)
    description=HTMLField()

    def __str__(self):
        return self.title


class CourseDetail(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    first=models.CharField(max_length=250,blank=True,null=True)
    second=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return self.first


class Blog(models.Model):
    title=models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)
    image=models.ImageField(upload_to="blog/")
    description=HTMLField()
    date=models.DateField(default=timezone.now)
    is_active=models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("web:blog-detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title    


class Enquiry(models.Model):
    QUALIFICATION_CHOICE = (("10th", "10th"), ("12th", "12th"),("Degree", "Degree"),("Diploma/ITI", "Diploma/ITI") )
    name=models.CharField(max_length=250)
    email=models.EmailField()
    address=models.CharField(max_length=250)
    phone_number=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20,choices=QUALIFICATION_CHOICE)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)
    message=models.TextField()
    
    def __str__(self):
        return self.name


class Career(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    phone_number=models.CharField(max_length=20)
    qualification=models.CharField(max_length=250)
    resume=models.FileField(upload_to="career/")
    
    def __str__(self):
        return self.name


class Gallery(models.Model):
    images=models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.images.url


class Expert(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='students/')
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name