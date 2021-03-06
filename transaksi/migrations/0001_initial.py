# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-25 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jurnal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('uraian', models.TextField()),
                ('debt', models.FloatField(blank=True, default=0.0)),
                ('kredit', models.FloatField(blank=True, default=0.0)),
                ('jurnal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaksis', to='jurnal.Jurnal')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'transaksi',
            },
        ),
    ]
