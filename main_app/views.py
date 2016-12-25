from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect


# Create your views here.
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        
	else:
		print  "invalid login details " + username + " " + password
        return render_to_response('login.html', {}, context)

		
def logout_view(request):
    logout(request)
    # Redirect to a success page.
	
def my_view(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    # ...