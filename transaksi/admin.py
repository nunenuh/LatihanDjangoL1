# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from transaksi.models import Transaksi
# Register your models here.

@admin.register(Transaksi)
class TransaksiAdmin(admin.ModelAdmin):
    pass