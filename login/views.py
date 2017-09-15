# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from login.forms import LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class LoginView(View):
    def get(self, request):
        template = 'login/login.html'
        form = LoginForm(request.POST or None)
        
        data = {
            'form': form
        }
        
        return render(request, template, data)
        
class ProsesLoginView(View):
    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth = authenticate(username=username, password=password)
            if auth:
                login(request, auth)

                return redirect('jurnal:view')

            return redirect('auth:view')

        return redirect('auth:view')

class ProsesLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('auth:view')

