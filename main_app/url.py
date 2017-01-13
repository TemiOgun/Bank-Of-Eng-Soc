from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views
from main_app.views import news

urlpatterns = [
url (r'^news/', news, name= 'news'),
#url('^change-password/$', auth_views.PasswordChangeView.as_view()),
#url('^change-password/$', auth_views.PasswordChangeView.as_view(template_name='change-password.html') ),

]