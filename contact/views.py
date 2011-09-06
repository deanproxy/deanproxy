from django.core.mail import send_mail
from django.shortcuts import render
from contact.forms import ContactForm

def index(request):
	return render(request, 'contact/index.html')

def send(request):
	to = 'dean@deanproxy.com'
	form = ContactForm(request.POST)
	if form.is_valid():
		message = form.cleaned_data['message']
		email = form.cleaned_data['email']
		message = 'From: %s\r\n\r\n' % email
		send_mail(
			'[deanproxy] Contact from website',
			message,
			email,
			[to],
			fail_silently=False
		)
		return render(request, 'contact/sent.html')
	return render(request, 'contact/index.html')
