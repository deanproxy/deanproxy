from django.http import HttpResponse
from django.shortcuts import redirect, render
from site_auth.models import Admin
from blog.views import login_required

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
		request.session['user_id'] = user.id

	return HttpResponse(status=status)

def logout(request):
	request.session['logged_in'] = False
	return redirect('/admin/')

@login_required
def password(request):
	return render(request, 'auth/reset.html')

@login_required
def reset_password(request):
	password_a = request.POST['password']
	password_b = request.POST['password_confirm']
	if password_a != password_b:
		return HttpResponse(status=400)
	else:
		try:
			user = Admin.objects.get(pk=request.session['user_id'])
		except Admin.DoesNotExist:
			return HttpResponse(status=500)
		else:
			user.password = Admin.make_password(password_a)
			user.save()
	return HttpResponse(status=200)


