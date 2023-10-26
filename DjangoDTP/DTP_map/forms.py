from django import forms


class DTPForm(forms.Form):
    region = forms.ChoiceField(label='region', widget=forms.Select)
    died = forms.IntegerField()
    year = forms.IntegerField()
