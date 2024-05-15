
from django.urls import path
from . import views


app_name = "web"

urlpatterns = [
    path("",views.IndexView.as_view(), name="index"),
    path("course/",views.CourseView.as_view(), name="course"),
    path("about/",views.AboutView.as_view(), name="about"),
    path("contact/",views.ContactView.as_view(), name="contact"),
    path("blog/",views.BlogView.as_view(), name="blog"),
    path("blog-detail/<slug:slug>/",views.BlogDetailView.as_view(), name="blog-detail"),
    path("career/",views.CareerView.as_view(), name="career"),
    path("gallery/",views.GalleryView.as_view(), name="gallery"),
]