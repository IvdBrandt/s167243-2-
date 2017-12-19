from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings






def contact(request):
    form = contactForm(request.POST or None)
    title = 'Contact form'
    confirm_message = None
    
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE.com'
        message = '%s %s' %(comment, name)
        emailTo = [settings.EMAIL_HOST_USER]
        emailFrom = form.cleaned_data['email']
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False,)
        title = 'Thanks'
        confirm_message = 'Thanks for the message, we will get back to you soon!'
        form = None
    context = {'title':title, 'form':form, 'confirm_message':confirm_message,}
    template = 'contact.html'
    return render(request, template, context)