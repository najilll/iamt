from web.forms import EnquiryForm

def main_context(request):
    return {

        'enquiry_form': EnquiryForm()

    }
