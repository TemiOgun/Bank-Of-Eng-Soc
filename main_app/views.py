
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render
from .models import alert

	
def login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		
		if user is not None:
			if user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect('/home')
			else:
				return HttpResponse("Your account is not currently active.")
		else:
			#print: "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request,'registration/login.html',{})

def news(request):
	return render(request,'base.html',{})

def home(request):
	alerts= alert.objects.all()
	context = {'alerts': alerts}
	if request.user.is_authenticated():
		return render(request,'mainpage.html', context)
	else:
		return render(request,'registration/login.html',{})
	
def financials(request):
	if request.user.is_authenticated():
		return render(request,'base.html',{})
	else:
		return render(request,'registration/login.html',{})

def rentals(request):
	if request.user.is_authenticated():
		return render(request,'base.html',{})
	else:
		return render(request,'registration/login.html',{})
	
def support(request):
	if request.user.is_authenticated():
		return render(request,'base.html',{})
	else:
		return render(request,'registration/login.html',{})

# def loggedin(request):
	# return render_to_response{}
	
# def logout(request):
	# auth.logout(request)
	
