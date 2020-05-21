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
    carousel1= "We value your health, stay safe"
    carousel2 = "All the family moments, captures in vivid shots"
    carousel3 = 'What is more valuable than celebrating true love, Uncle S Studio Freezes these moments for you'
    carousel4 = "We make all you memories count"
    #context= {'name':name}
    return render(request, 'index.html',{'page':name, 'carousel1':carousel1, 'carousel2':carousel2,'carousel3':carousel3,'carousel4':carousel4})

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

            email = EmailMessage("New contact form submission",content,"info@samizzoventures.com" +'',
                ['info@samizzoventures.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')
    return render(request, 'contact.html', {'page':name, 'form':form})



def Employees(request):
    Employees = models.Employees
    page = 'About Us'
    e_list = Employees.objects.all()
    return render(request, 'portfolio.html', {'team':e_list,})