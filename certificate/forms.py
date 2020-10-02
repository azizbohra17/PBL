from django import forms
from datetime import datetime, date


class CertificateOfParticipationForm(forms.Form):
    name = forms.CharField()
    fest = forms.CharField()
    date = forms.DateField()
    event_name = forms.CharField()

