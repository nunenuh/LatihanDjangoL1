# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jurnal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jurnals')
    nama = models.CharField(max_length=30)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'jurnal'
        ordering = ['-id']