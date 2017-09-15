from django import forms
from transaksi.models import Transaksi

class DateInput(forms.DateInput):
    input_type = 'date'

class TransaksiForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    
    tanggal = forms.CharField(widget=DateInput(), max_length=100)
    uraian = forms.CharField(widget=forms.Textarea)
    debt = forms.CharField(max_length=100)
    kredit = forms.CharField(max_length=100)
    
    

    class Meta:
        model = Transaksi