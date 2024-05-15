from django import forms

from .models import Enquiry,Contact,Career

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        exclude = ()

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Your name:",
                    }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control required email",
                    "placeholder": "Your Mail:",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Enter Your number:",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control required",
                    "placeholder": "Your address:",
                }
            ),
            "qualification": forms.Select(
                attrs={
                    "class": "form-control required",
                    "placeholder": "choose Your qualification:",
                }
            ),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "required",
                       "placeholder": "Your name:",
                    }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "required email",
                    "placeholder": "Your Mail:",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "required",
                    "placeholder": "Enter Your number:",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "required",
                    "placeholder": "Your message:",
                }
            ),
        }


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        exclude = ()

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "required",
                       "placeholder": "Your name:",
                    }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "required email",
                    "placeholder": "Your Mail:",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "required",
                    "placeholder": "Enter Your number:",
                }
            ),
            "qualification": forms.TextInput(
                attrs={
                    "class": "required",
                    "placeholder": "Your higher qualification:",
                }
            ),
            "resume": forms.FileInput(
                attrs={
                    "class": "required",
                    "placeholder": "Drop Your Resume/CV Here:",
                }
            ),
        }