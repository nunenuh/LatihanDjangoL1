# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from jurnal.models import Jurnal
from django.http import HttpResponse
from jurnal.forms import JurnalForm
from django.contrib.auth.mixins import LoginRequiredMixin

class HarusLogin(LoginRequiredMixin):
    login_url = '/login/'

class ListJurnalView(HarusLogin, View):
    
    def get(self, request):
        template = 'jurnal/jurnal.html'

        jurnals = Jurnal.objects.all()

        data = {
            'list_jurnal': jurnals, 
            'test': 'rinjanii'
        }

        return render(request, template, data)

class TambahJurnalView(HarusLogin, View):
    def get(self, request):
        template = 'jurnal/tambah_jurnal.html'

        form = JurnalForm(request.POST or None)
        data = {
            'form': form,
        }

        return render(request, template, data)

class SimpanJurnalView(View):

    def post(self, request):
        template = 'jurnal/tambah_jurnal.html'

        form = JurnalForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            jurnal = Jurnal()
            jurnal.user = request.user
            jurnal.nama = form.cleaned_data['nama']
            jurnal.keterangan = form.cleaned_data['keterangan']
            jurnal.save()
            
            return redirect('jurnal:view')
        else:
            
            data = {
                'form': form,
            }

            return render(request, template, data)



class HapusJurnalView(View):

    def get(self, request, nomer):
        jr = Jurnal.objects.filter(pk=nomer)
        if jr.exists():
            jr = jr.first()
            jr.delete()
        return redirect('jurnal:view')
    
class EditJurnalView(View):
    def get(self, request, nomer):
        template = 'jurnal/edit_jurnal.html'

        jr = Jurnal.objects.get(pk=nomer)
        jurnal_data = {
            'id': jr.id,
            'nama': jr.nama,
            'keterangan': jr.keterangan
        }

        form = JurnalForm(request.POST or None, initial=jurnal_data)
        data = {
            'form': form,
        }

        return render(request, template, data)

class UpdateJurnalView(View):
    
    def post(self, request):
        template = 'jurnal/tambah_jurnal.html'

        form = JurnalForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            jurnal = Jurnal.objects.get(pk=id)
            jurnal.user = request.user
            jurnal.nama = form.cleaned_data['nama']
            jurnal.keterangan = form.cleaned_data['keterangan']
            jurnal.save(force_update=True)
            
            return redirect('jurnal:view')
        else:
            
            data = {
                'form': form,
            }

            return render(request, template, data)