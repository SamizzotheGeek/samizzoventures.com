from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import ContactForm
from django.template.loader import get_template
from . import models
#from django.http import Http404
# Create your views here.
def index(request):
    name = 'SAMIZZO VENTURES'
    return render(request, 'index.html',{'page':name})

def contact(request):
    name = "Contact Us"
    form = ContactForm
    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name', '')
            contact_email = request.POST.get(
                'contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage("New contact form submission",content,"info@samizzoventures.co.ke" +'',
                ['info@samizzoventures.co.ke'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')
    return render(request, 'contact.html', {'page':name, 'form':form})



def Members(request):
    Members = models.Team
    page = 'About Us'
    m_list = Members.objects.all()
    desc = open('home/description.txt')
    description = desc.read()
    desc.close()
    return render(request, 'about.html', {'team':m_list,'description':description, 'page':page})

    