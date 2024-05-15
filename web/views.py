from django.shortcuts import render,redirect
from django.views.generic import TemplateView,DetailView,ListView,CreateView
from . models import Career, CourseOverview, Gallery, Testimonial,Course,CourseDetail,CourseFeactures,Blog,Enquiry
from .forms import CareerForm, EnquiryForm,ContactForm
import urllib.parse
from django.views.generic import FormView
from django.http import JsonResponse
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name = "web/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonial"] = Testimonial.objects.filter(is_active=True)
        context["blogs"] = Blog.objects.filter(is_active=True)
        return context
    

class CourseView(TemplateView,FormView):
    template_name = "web/course.html"
    form_class = EnquiryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = Course.objects.first()
        context["course_features"] = CourseFeactures.objects.all()
        context["course_details"] = CourseDetail.objects.all()
        context["overview"] = CourseOverview.objects.filter(title='overview')[:1]
        context["training_structure"] = CourseOverview.objects.filter(title='training_structure')
        context["eligibility"] = CourseOverview.objects.filter(title='eligibility')
        context["facilities"] = CourseOverview.objects.filter(title='facilities')
        return context
    
    def form_valid(self, form):
        service = Course.objects.first()  # Assuming you want to use the first course
        form.instance.service = service
        form.save()

        data = form.cleaned_data

        message = (
            f'Name: {data["name"]} \n'
            f'Phone: {data["phone_number"]} \n'
            f'Email: {data["email"]} \n'
            f'Address: {data["address"]} \n'
            f'Qualification: {data["qualification"]} \n'
        )

        whatsapp_api_url = "https://api.whatsapp.com/send"
        phone_number = "+9037126305"  # Change to your desired phone number
        encoded_message = urllib.parse.quote(message)
        whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"

        # Redirect to the WhatsApp link
        return redirect(whatsapp_url)

    def form_invalid(self, form):
        errors = form.errors
        print(errors)
        response_data = {"status": "false", "title": "Form validation error"}
        return JsonResponse(response_data, status=400)

class AboutView(TemplateView):
    template_name = "web/about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonial"] = Testimonial.objects.filter(is_active=True)
        context["blogs"] = Blog.objects.filter(is_active=True)
        return context


class ContactView(TemplateView,FormView):
    template_name = "web/contact.html"
    form_class = ContactForm

    def get(self, request):
        form = ContactForm()
        context = {
            "form": form,
        }
        return render(request, "web/contact.html", context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Our team will contact you soon !!",
                'redirect' :True
            }
            return JsonResponse(response_data)
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({"status": "false", "errors": errors}, status=400)



class BlogView(ListView):
    model=Blog
    template_name = "web/blog.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["blogs"] = Blog.objects.filter(is_active=True)
    #     return context
    

class BlogDetailView(DetailView):
    model=Blog
    template_name = "web/blog-details.html"


class CareerView(CreateView):
    model=Career
    template_name = "web/career.html"
    form_class = CareerForm

    def get_success_url(self):
        return reverse_lazy('web:index')


class GalleryView(TemplateView):
    template_name = "web/gallery.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = Gallery.objects.all()

        return context