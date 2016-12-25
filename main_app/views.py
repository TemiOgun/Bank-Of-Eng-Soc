from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect



def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
		login(request, user)
        # Redirect to a success page.
    else:
		print "log in failed"
		return HttpResponse("Invalid login details supplied")
        # Return an 'invalid login' error message.
		