from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.contrib import messages
from .models import ContactMessage

def submit_contact(request):
    if request.method == 'POST':
        # Extract data from the HTML form securely
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save it directly to the database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Trigger a Django success message
        messages.success(request, "Message sent successfully! I'll get back to you soon.")
        
        # Redirect back to the contact section to clear the form
        return redirect('/#contact')
        
    # If someone tries to access the URL directly without submitting a form, send them home
    return redirect('/')