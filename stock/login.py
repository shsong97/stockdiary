# -*- coding: utf-8 -*-

from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.


from django.core.paginator import Paginator
from django.db.models import Q
from forms import *

login_url = '/stock/login/'

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_page(request):
    next ='/'

    if request.GET:
        if request.GET['next']:
            next=request.GET['next']
    
    if request.POST:
        username = request.POST['id_username']
        password = request.POST['id_password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect(next)
            else:
                # Return a 'disabled account' error message
                return HttpResponse("<script>alert('disabled accout'); window.location='" + login_url + "';</script>")
        else:
            # Return an 'invalid login' error message.
            return HttpResponse("<script>alert('invalid accout'); window.location='" + login_url + "';</script>")

    return render_to_response('registration/login.html', RequestContext(request))


def register_success(request):
    return render_to_response('registration/register_success.html', RequestContext(request))


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )

            return HttpResponseRedirect('success/')
    else:
        form = RegistrationForm()

    variables = RequestContext(request, {'form': form})
    return render_to_response('registration/register.html', variables)



