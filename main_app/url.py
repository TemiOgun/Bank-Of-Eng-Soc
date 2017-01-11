from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

url('^change-password/$', auth_views.PasswordChangeView.as_view()),
#url('^change-password/$', auth_views.PasswordChangeView.as_view(template_name='change-password.html') ),

]