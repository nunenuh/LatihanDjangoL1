from django import forms
from jurnal.models import Jurnal

class JurnalForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    nama = forms.CharField(max_length=100)
    keterangan = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Jurnal