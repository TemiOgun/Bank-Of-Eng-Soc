from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('registration/login.html', c)
	
def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('login')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def home(request):
	return render_to_response('base.html')
# def loggedin(request):
	# return render_to_response{}
	
# def logout(request):
	# auth.logout(request)
	
