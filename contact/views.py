from django.shortcuts import redirect
from django.contrib import messages
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
        
        # FIX: Check if the request is an AJAX request from our JavaScript
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # We MUST return JSON here for the animation to trigger
            return JsonResponse({'status': 'success', 'message': 'Message sent!'})
            
        # Fallback for standard submission
        messages.success(request, "Message sent successfully!")
        return redirect('/#contact')
        
    return redirect('/')