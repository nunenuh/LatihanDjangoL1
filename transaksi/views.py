# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from jurnal.models import Jurnal
from transaksi.models import Transaksi
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from transaksi.forms import TransaksiForm
# Create your views here.

class HarusLogin(LoginRequiredMixin):
    login_url = '/login/'

class ListTransaksiView(HarusLogin, View):
    
    def get(self, request, jurnal_id):
        template = 'transaksi/index.html'
        jurnal = Jurnal.objects.get(pk=jurnal_id)
        transaksis = Transaksi.objects.filter(jurnal__id=jurnal_id)

        form = TransaksiForm(request.POST or None)

        data = {
            'jurnal': jurnal,
            'transaksis': transaksis, 
            'form': form,
            'form_mode': 'add',
        }

        return render(request, template, data)


class SimpanTransaksiView(HarusLogin, View):

    def post(self, request, jurnal_id):
        template = 'transaksi/index.html'

        form = TransaksiForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            jurnal = Jurnal.objects.get(pk=jurnal_id)
            tr = Transaksi()
            tr.jurnal = jurnal
            tr.tanggal = form.cleaned_data['tanggal']
            tr.uraian = form.cleaned_data['uraian']
            tr.debt = form.cleaned_data['debt']
            tr.kredit = form.cleaned_data['kredit']
            tr.save()
            
            return redirect('transaksi:view', jurnal_id=jurnal_id)
        else:
            jurnal = Jurnal.objects.get(pk=jurnal_id)
            transaksis = Transaksi.objects.filter(jurnal__id=jurnal_id)
            form = TransaksiForm(request.POST or None)

            data = {
                'jurnal': jurnal,
                'transaksis': transaksis, 
                'form': form,
                'form_mode': 'add',
            }

            return render(request, template, data)

class EditTransaksiView(View):
    def get(self, request, jurnal_id, transaksi_id):
        template = 'transaksi/index.html'

        jurnal = Jurnal.objects.get(pk=jurnal_id)
        transaksi = Transaksi.objects.get(pk=transaksi_id)
        transaksis = Transaksi.objects.filter(jurnal__id=jurnal_id)

        data_transaksi = {
            'id': transaksi.id,
            'tanggal': transaksi.tanggal,
            'uraian': transaksi.uraian,
            'debt': transaksi.debt,
            'kredit': transaksi.kredit
        }

        form = TransaksiForm(request.POST or None, initial=data_transaksi)

        data = {
            'jurnal': jurnal,
            'form': form,
            'transaksis': transaksis,
            'form_mode': 'edit'
        }

        return render(request, template, data)

class UpdateTransaksiView(View):
    def post(self, request, jurnal_id):
        template = 'transaksi/index.html'

        form = TransaksiForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            id = form.cleaned_data['id']
            jurnal = Jurnal.objects.get(pk=jurnal_id)
            tr = Transaksi.objects.get(pk=id)
            tr.jurnal = jurnal
            tr.tanggal = form.cleaned_data['tanggal']
            tr.uraian = form.cleaned_data['uraian']
            tr.debt = form.cleaned_data['debt']
            tr.kredit = form.cleaned_data['kredit']
            tr.save(force_update=True)
            
            return redirect('transaksi:view', jurnal_id=jurnal_id)
        else:
            jurnal = Jurnal.objects.get(pk=jurnal_id)
            transaksis = Transaksi.objects.filter(jurnal__id=jurnal_id)
            form = TransaksiForm(request.POST or None)

            data = {
                'jurnal': jurnal,
                'transaksis': transaksis, 
                'form': form,
                'form_mode': 'edit',
            }

            return render(request, template, data)

class HapusTransaksiView(View):
    def get(self, request, jurnal_id, transaksi_id):
        jurnal = Jurnal.objects.get(pk=jurnal_id)
        trx = Transaksi.objects.get(jurnal=jurnal, pk=transaksi_id)
        if trx:
            trx.delete()

        return redirect('transaksi:view', jurnal_id=jurnal_id)