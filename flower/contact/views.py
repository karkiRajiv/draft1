from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .forms import *

# def contacts(request):
#     return render(request,'contact.html')


def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('contact_form.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_content': contact_content,
            }

            content = template.render(context)

            email = EmailMessage(
                "New message from customer",
                content,
                "Pharmacy" + '',
                ['aavashneupane4@gmail.com'],
                headers={'Reply To': contact_email}
            )

            email.send()

            messages.success(request, f'Your message has been sent!')
            return redirect('contact')

    return render(request, 'contact.html', {'form': Contact_Form})