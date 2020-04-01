from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'home.html', {})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        #send mail
        send_mail(
            name, #subject
            message, #message
            email, #from email
            ['dnyingifa@gmail.com'], # to email
            fail_silently = False,
        )

        return render(request, 'contact.html', {'name':name})
    else:
        return render(request, 'contact.html', {})