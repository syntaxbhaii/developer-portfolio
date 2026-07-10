from django.shortcuts import render
# Create your views here.
from django.shortcuts import redirect
from django.contrib import messages
from .models import ContactMessage
from django.http import JsonResponse
from .models import ContactMessage
def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        
        # Check if the request is an AJAX request from our JavaScript
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success', 'message': 'Message sent!'})
            
        # Fallback for standard submission
        messages.success(request, "Message sent successfully!")
        return redirect('/#contact')
        
    return redirect('/')