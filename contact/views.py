from django.core.mail.message import EmailMessage
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
		mail = EmailMessage(
			'[deanproxy] Contact from website',
			message,
			email,
			[to],
			headers={'Reply-To':email}
		)
		mail.send()
		return render(request, 'contact/sent.html')
	return render(request, 'contact/index.html')
