from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect

# Create your views here.

@csrf_protect
def login(request):
	args = {}
	#args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		print(user.username)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error'] = 'No such user'
			return render(request, 'auth_app/login.html', args)
	else:
		return render(request, 'auth_app/login.html', args)

def logout(request):
	auth.logout(request)
	return redirect('/')
