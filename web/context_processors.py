from web.forms import EnquiryForm

def main_context(request):
    # Your other context data
    return {
        # Your other context data
        'e_form': EnquiryForm()
        # Your other context data
    }
