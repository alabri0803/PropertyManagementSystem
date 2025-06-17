from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.utils.translation import gettext as _


def home(request):
  return render(request, 'core/home.html', {'title': _('Home Page')})