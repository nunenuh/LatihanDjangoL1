# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from jurnal.models import Jurnal
# Register your models here.

@admin.register(Jurnal)
class JurnalAdmin(admin.ModelAdmin):
    pass