from django.http import HttpResponse
from django.shortcuts import redirect, render
from auth.models import Admin

def index(request):
	return render(request, 'auth/login.html')

def login(request):
	status = 200
	try:
		user = Admin.authenticate(request.POST['username'], request.POST['password'])
	except Admin.DoesNotExist:
		status = 401
	except Admin.PermissionDenied:
		status = 401
	else:
		request.session['logged_in'] = True

	return HttpResponse(status=status)

def logout(request):
	request.session['logged_in'] = False
	return redirect('/admin/')


