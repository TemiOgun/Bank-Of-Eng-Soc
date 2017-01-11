"""BankOfEngSoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from main_app import views as main_views
from main_app import url as main_urls

urlpatterns = [
	url(r'^login/$', main_views.login),
	url(r'^home/$', main_views.home, name = 'home'),
	url(r'^financials/$', main_views.financials, name = 'financials'),
	url(r'^rentals/$', main_views.rentals, name = 'rentals'),
	url(r'^support/$', main_views.support, name = 'support'),
	url(r'^logout/$', auth_views.logout),
	url(r'^admin/', admin.site.urls)
]
