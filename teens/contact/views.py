from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
from .models import Question

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            content = request.POST.get('content', '')
            #creamos correo
            email = EmailMessage(
                "Chocolates Teens: Mensaje de contacto",
                "De {} <{}>\n\nTema: {}\n\n{}".format(name, email, subject, content),
                "no-contestar@inbox.mailtrap.io",
                reply_to=[email]
            )
            #Enviamos y redireccionamos
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")
    #FAQ
    questions = Question.objects.all()[:3]
    context = {'form' : contact_form, 'questions' : questions}
    return render(request, 'contact/contact.html', context)