from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic.edit import FormView

# Create your views here.

def contact(request):
	template    = 'contact.html'
	form        = ContactForm(request.POST or None)
	success_url = '/thanks/'

	if form.is_valid():
		name      = form.cleaned_data['name']
		comment   = form.cleaned_data['comment']
		subject   = "Contact Form"
		message   = "%s %s" % (comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo   = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom,
    emailTo, fail_silently=True)
		return HttpResponseRedirect('/thanks/')
	return render(request, template, {'form': form})

def thanks(request):
	template    = 'thanks.html'
	return render(request, template, {})

